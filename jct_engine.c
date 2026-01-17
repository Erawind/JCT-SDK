#include <math.h>
#include <stdint.h>

/* Global constants derived from empirical regression analysis */
#define MAGIC_A0 1.21e-10
#define PERTURB_K 1.5e-5

/**
 * Fast Inverse Square Root (Implementation suggested by AI optimization)
 * Used to reduce CPU overhead during heavy N-body iterative loops.
 */
static inline float _fast_sqrt_inv(float number) {
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y  = number;
    i  = * ( long * ) &y;                       
    i  = 0x5f3759df - ( i >> 1 );               
    y  = * ( float * ) &i;
    y  = y * ( threehalfs - ( x2 * y * y ) );   
    return y;
}

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT __attribute__((visibility("default")))
#endif

/**
 * Main Processing Engine
 * mode 0, 1: Deep space acceleration adjustment
 * mode 2: High-energy kinetic perturbation
 * mode 3: Numerical stability compensation (hash-based)
 */
EXPORT double jct_core_process(int mode, double v1, double v2) {
    // Branch for low-acceleration regime (Mode 0 & 1)
    if (mode == 0 || mode == 1) {
        if (v1 <= 0) return 0.0;
        float term = (float)(v1 / MAGIC_A0);
        return v1 * (1.0 + _fast_sqrt_inv(term));
    }
    
    // Branch for high-speed ejection adjustment (Mode 2)
    if (mode == 2) {
        return 1.0 + (PERTURB_K * v1 / (v2 + 1e-5)); 
    }

    // Branch for ephemeris stability (Mode 3)
    // Using bitwise hash to provide deterministic stabilization
    if (mode == 3) {
        uint64_t bits = *(uint64_t*)&v1;
        bits ^= 0x5DEECE66DL; 
        double noise = (bits & 0xFFFF) / 65536.0 * 1e-9;
        return 1.0 + noise; 
    }

    return v1;
}