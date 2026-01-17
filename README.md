# JCT: Jinyan's Computational Toolkit (v1.0)

**[English]** | **[中文說明]**

## 🌌 Overview / 概覽
**[EN]** JCT is a high-performance numerical toolkit designed to address residuals in galaxy rotation curves and JWST early galaxy data via a $1.21 \times 10^{-10} \text{ m/s}^2$ threshold patch.
**[中文]** JCT 是一個高效能數值工具庫，透過 $1.21 \times 10^{-10} \text{ m/s}^2$ 加速度閾值修正，解決星系旋轉曲線殘差與 JWST 早期星系數據偏差。

---

## 🛠 Technical Specifications / 技術規格

| Feature / 特性 | Specification / 規格 | Purpose / 目的 |
| :--- | :--- | :--- |
| **Threshold ($a_0$)** | $1.21 \times 10^{-10} \text{ m/s}^2$ | Defines the correction boundary / 定義修正邊界 |
| **Correction Logic** | $a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$ | Reconciles RAR / 對齊徑向加速度關係 |
| **Computing Core** | Native C (O3 Optimized) | High-throughput N-Body / 大規模質點模擬 |



---

## 💻 Usage / 使用範例

```bash
# Build C core / 編譯核心
gcc -O3 -shared -fPIC -o jct_engine.so jct_engine.c
