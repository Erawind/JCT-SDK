# JCT: Jinyan's Computational Toolkit (v1.0)

> **[English Navigation]** | **[中文快速跳轉](#jct-jinyans-computational-toolkit-中文說明)**

---

## 🌌 Overview (英文簡介)
JCT is a lightweight, high-performance numerical calibration toolkit designed for astronomical N-body simulations and observational data alignment. 

By implementing an empirical **acceleration-threshold patch** ($a_0 \approx 1.21 \times 10^{-10} \text{ m/s}^2$), JCT addresses systematic residuals often found in:
* **Galaxy Rotation Curves**: Resolving the velocity "drop-off" in the low-acceleration regime (consistent with the SPARC database).
* **Early Galaxy Morphology**: Stabilizing high-redshift ($z > 7$) mass-luminosity structures, addressing the "Impossible Early Galaxy" problem identified by JWST.
* **Cosmological Tensions**: Providing numerical pathways to mitigate the **$S_8$ Tension**.
* **Long-term Stability**: Enhancing ephemeris stability and reducing numerical drift.

> **Note:** This toolkit is strictly **data-driven**. It implements optimized empirical parameters derived from extensive residual analysis.

---

## 🛠 Technical Specifications (技術規格)

| Feature / Parameter | Specification | Purpose |
| :--- | :--- | :--- |
| **Critical Threshold ($a_0$)** | $1.21 \times 10^{-10} \text{ m/s}^2$ | Defines the boundary for gravitational correction |
| **Correction Logic** | $a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$ | Reconciles RAR (Radial Acceleration Relation) |
| **Computational Core** | Native C (IEEE 754 Optimized) | Maximizes N-body throughput ($N > 10^5$) |
| **Compatibility** | Python 3.x / NumPy / SciPy | Seamless integration for researchers |



---

## 💻 Installation & Usage (安裝與使用)

### 1. Build the Engine
```bash
# Compile the C core into a shared library
gcc -O3 -shared -fPIC -o jct_engine.so jct_engine.c
