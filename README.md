JCT: Jinyan's Computational Toolkit (v1.0)



**[English]** | [中文說明](#jct-jinyans-computational-toolkit-中文說明)



---



## 🌌 Overview

JCT is a lightweight, high-performance numerical calibration toolkit designed for astronomical N-body simulations and observational data alignment. 



By implementing an empirical **acceleration-threshold patch** ($a_0 \approx 1.21 \times 10^{-10} \text{ m/s}^2$), JCT addresses systematic residuals often found in:

* **Galaxy Rotation Curves**: Resolving the velocity "drop-off" in the low-acceleration regime (consistent with the SPARC database).

* **Early Galaxy Morphology**: Stabilizing high-redshift ($z > 7$) mass-luminosity structures, addressing the "Impossible Early Galaxy" problem identified by JWST.

* **Cosmological Tensions**: Providing numerical pathways to mitigate the **$S_8$ Tension**.

* **Long-term Stability**: Enhancing ephemeris stability and reducing numerical drift.



> **Note:** This toolkit is strictly **data-driven**. It implements optimized empirical parameters derived from extensive residual analysis.



---



## 🛠 Technical Specifications



| Feature / Parameter | Specification | Purpose |

| :--- | :--- | :--- |

| **Critical Threshold ($a_0$)** | $1.21 \times 10^{-10} \text{ m/s}^2$ | Defines the boundary for gravitational correction |

| **Correction Logic** | $a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$ | Reconciles RAR (Radial Acceleration Relation) |

| **Computational Core** | Native C (IEEE 754 Optimized) | Maximizes N-body throughput ($N > 10^5$) |



---



## 💻 Installation & Usage



```bash

# Build the C core

gcc -O3 -shared -fPIC -o jct_engine.so jct_engine.c

---

```

## 🏮 JCT: Jinyan's Computational Toolkit 中文說明



JCT 是一個輕量級、高效能的數值校準工具庫，專為天文 N-body 模擬與觀測數據對齊而設計。



透過引入基於數據驅動的 **加速度閾值修正** ($a_0 \approx 1.21 \times 10^{-10} \text{ m/s}^2$)，JCT 致力於解決以下場景中的系統性殘差 (Residuals)：



1. **星系旋轉曲線**：修正低加速度區域的速度偏移。

2. **早期星系形態**：穩定高紅移 ($z > 7$) 質量-光度結構，解決 JWST 觀測穩定性問題。

3. **宇宙學張力**：為緩解 **$S_8$ Tension** 結構增長問題提供數值路徑。

4. **長期穩定性**：提升深空軌道積分過程中的星曆穩定性，減少數值漂移。



### 技術規格

| 特性 / 參數 | 規格描述 | 應用目的 |

| :--- | :--- | :--- |

| **臨界閾值 ($a_0$)** | $1.21 \times 10^{-10} \text{ m/s}^2$ | 定義引力修正的物理邊界 |

| **校正邏輯** | $a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$ | 對齊 RAR (徑向加速度關係) |

| **計算核心** | 原生 C 語言 (O3 優化) | 支持大規模模擬 |



### 開發與免責聲明

* **AI 輔助**：本工具採用 AI 輔助編寫，以優化 C 語言核心效能。

* **免責聲明**：本專案為獨立開發，僅供參考，不保證結果正確性。



---

Maintained by Jinyan. Released under MIT License.
