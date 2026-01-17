import ctypes, os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DLL_PATH = os.path.join(BASE_DIR, "jct_engine.dll") 
class JCTEngine: 
    def __init__(self): 
        try: 
            self._lib = ctypes.CDLL(DLL_PATH) 
            self._lib.jct_core_process.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_double] 
            self._lib.jct_core_process.restype = ctypes.c_double 
        except: self._lib = None 
    def _call(self, m, v1, v2=0.0): 
        return self._lib.jct_core_process(int(m), float(v1), float(v2)) if self._lib else v1 
_eng = JCTEngine() 
def correct_galaxy_rotation(a): return _eng._call(0, a) 
def ephemeris_stability_index(v): return _eng._call(3, v)