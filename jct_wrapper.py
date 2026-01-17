import ctypes
import os
import platform

# 自動載入
lib_path = "./jct_engine.dll" if platform.system() == "Windows" else "./jct_engine.so"

try:
    _lib = ctypes.CDLL(lib_path)
    # 這裡必須對應你剛才那份 C 代碼的函數名稱：jct_core_process
    _lib.jct_core_process.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double]
    _lib.jct_core_process.restype = ctypes.c_double

    def correct_acceleration(acc_newton):
        # 執行你 code 裡的 mode 0
        return _lib.jct_core_process(0, acc_newton, 0.0)

except OSError:
    print("C engine not found, please compile first.")
