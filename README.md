\# JCT: Jinyan's Computational Toolkit (v1.0)



\*\*\[English]\*\* | \[中文說明](#中文說明)



\## Overview

JCT is a lightweight, high-performance numerical correction library designed for astronomical N-body simulations and observational data calibration. 



It addresses systematic residuals often found in:

\* Galaxy rotation curves (low-acceleration regime).

\* High-redshift mass-luminosity relations (JWST early data).

\* Long-term ephemeris stability in numerical integration.



\*\*Note:\*\* This toolkit is purely \*\*data-driven\*\*. It implements optimized empirical fitting parameters and numerical compensation techniques derived from extensive residual analysis.



\## Development Note

\*\*Note: This SDK was developed with AI coding assistance.\*\*



\## Features

\* \*\*Heterogeneous Core\*\*: The underlying engine is written in C for maximum performance.

\* \*\*Empirical Fitting\*\*: Corrections are based on statistical regression of observational datasets.

\* \*\*Plug-and-Play\*\*: Python wrapper included for seamless integration into existing scientific workflows (NumPy/SciPy compatible).



\## Installation \& Usage



Compile the core engine and import the Python wrapper:



```bash

\# Compile the shared library

gcc -O3 -shared -fPIC -o jct\_engine.so jct\_engine.c  # Linux/macOS

\# or

gcc -O3 -shared -o jct\_engine.dll jct\_engine.c       # Windows



Python Example

from jct import correct\_galaxy\_rotation, ephemeris\_stability\_index



\# Example 1: Correcting Newtonian acceleration prediction

acc\_newton = 1.2e-11

acc\_corrected = correct\_galaxy\_rotation(acc\_newton)

print(f"Corrected: {acc\_corrected}")



\# Example 2: Getting stability factor for N-body simulation

stability\_factor = ephemeris\_stability\_index(12.5)



Disclaimer

This is an independent personal project. The software and data are provided "as is" for reference purposes only. The author makes no warranties regarding the correctness of the results or any consequences arising from their use.





JCT: Jinyan's Computational Toolkit (中文說明)



JCT 是一個輕量級、高效能的數值校準工具庫，專為天文 N-body 模擬與觀測數據處理而設計。



本工具主要解決以下場景中常見的數值殘差 (Residuals)：



星系旋轉曲線（低加速度區域）。

高紅移質量-光度關係（JWST 早期宇宙數據）。

數值積分過程中的長期星曆穩定性。

注意： 本工具完全基於數據驅動 (Data-driven)。所有修正項均來自對觀測數據的統計擬合與演算法優化。



開發註記

注意：本 SDK 採用 AI 進行輔助編寫。



核心特性

異構核心 (Heterogeneous Core)：底層運算採用 C 語言編寫以追求最高效能。

經驗擬合 (Empirical Fitting)：所有參數均源自對大量觀測數據的殘差分析。

即插即用：提供 Python 封裝接口，可輕鬆整合進現有的科學計算流程（相容 NumPy/SciPy）。



免責聲明

本專案為私人獨立開發。所有代碼與數據僅供參考。作者不對結果的正確性做任何保證，亦不承擔因使用本工具而產生的任何責任。



Maintained by Jinyan. Released under MIT License.

