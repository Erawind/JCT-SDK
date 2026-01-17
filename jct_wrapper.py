import ctypes
import os
import platform

# 1. 載入 C 核心引擎 (Loading the C engine)
lib_path = ""
system = platform.system()

if system == "Windows":
    lib_path = "./jct_engine.dll"
else:
    lib_path = "./jct_engine.so"

try:
    # 載入共享庫
    _lib = ctypes.CDLL(lib_path)
    
    # 2. 定義 C 函數的參數與回傳類型 (Specifying argtypes & restype)
    # 假設 C 函數原型為: double jct_correct(double a_newton)
    _lib.jct_correct.argtypes = [ctypes.c_double]
    _lib.jct_correct.restype = ctypes.c_double
    
    def correct_acceleration(acc_newton):
        """
        傳入牛頓加速度，回傳 JCT 修正後的加速度。
        Threshold: 1.21e-10 m/s^2
        """
        return _lib.jct_correct(acc_newton)

except OSError:
    print(f"[JCT-SDK] Warning: Could not find '{lib_path}'.")
    print("Please compile jct_engine.c first to use high-performance mode.")
    
    # 3. 如果找不到 C 庫，提供一個純 Python 備援方案 (Fallback)
    def correct_acceleration(acc_newton):
        a0 = 1.21e-10
        if acc_newton <= 0: return 0
        return acc_newton * (1.0 + (a0 / acc_newton)**0.5)

def get_stability_index(radius_kpc):
    """計算特定軌道半徑下的數值穩定指標"""
    # 簡單的線性縮放範例，可根據需求修改
    return 1.0 / (1.0 + radius_kpc * 0.01)
