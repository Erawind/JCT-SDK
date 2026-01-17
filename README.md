JCT: Jinyan's Computational Toolkit (v1.0)[English] | 中文說明OverviewJCT is a lightweight, high-performance numerical calibration toolkit designed for astronomical N-body simulations and observational data alignment.By implementing an empirical acceleration-threshold patch ($a_0 \approx 1.21 \times 10^{-10} \text{ m/s}^2$), JCT addresses systematic residuals often found in:Galaxy Rotation Curves: Resolving the velocity "drop-off" in the low-acceleration regime (consistent with the SPARC database).Early Galaxy Morphology: Stabilizing high-redshift ($z > 7$) mass-luminosity structures, addressing the "Impossible Early Galaxy" problem identified by JWST.Cosmological Tensions: Providing numerical pathways to mitigate the $S_8$ Tension by adjusting structure growth rates in the low-acceleration limit.Long-term Stability: Enhancing ephemeris stability and reducing numerical drift in long-cycle deep-space integrations.Note: This toolkit is strictly data-driven. It implements optimized empirical parameters derived from extensive residual analysis of observational datasets.Technical SpecificationsFeature / ParameterSpecificationPurposeCritical Threshold ($a_0$)$1.21 \times 10^{-10} \text{ m/s}^2$Defines the boundary for gravitational correctionCorrection Logic$a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$Reconciles RAR (Radial Acceleration Relation)Computational CoreNative C (IEEE 754 Optimized)Maximizes N-body throughput ($N > 10^5$)PrecisionDouble-precision Floating PointMinimizes numerical drift in long-term orbitsCompatibilityPython 3.x / NumPy / SciPySeamless integration for researchersInstallation & Usage1. Build the EngineBash# Compile the C core into a shared library
# Linux/macOS
gcc -O3 -shared -fPIC -o jct_engine.so jct_engine.c 

# Windows (MinGW)
gcc -O3 -shared -o jct_engine.dll jct_engine.c
2. Python API ExamplePythonimport jct_wrapper as jct

# Example 1: Calculating corrected acceleration for a galaxy fringe
acc_raw = 0.5e-11  # Typical acceleration at galaxy edge (m/s^2)
acc_jct = jct.correct_acceleration(acc_raw)
print(f"Newtonian: {acc_raw} | JCT Enhanced: {acc_jct}")

# Example 2: Checking stability index for a specific orbital radius (kpc)
stability = jct.get_stability_index(radius_kpc=25.0)
print(f"Orbital Stability Factor: {stability}")
JCT: Jinyan's Computational Toolkit (中文說明)JCT 是一個輕量級、高效能的數值校準工具庫，專為天文 N-body 模擬與觀測數據對齊而設計。透過引入基於數據驅動的加速度閾值修正 ($a_0 \approx 1.21 \times 10^{-10} \text{ m/s}^2$)，JCT 致力於解決以下場景中的系統性殘差 (Residuals)：星系旋轉曲線：修正低加速度區域的速度掉落（與 SPARC 數據庫觀測結果一致）。早期星系形態：穩定高紅移 ($z > 7$) 質量-光度結構，解決 JWST 觀測到的「不可能的早期星系」穩定性矛盾。宇宙學張力：透過調整低加速度下的結構增長率，為緩解 $S_8$ Tension 問題提供數值路徑。長期穩定性：提升深空軌道積分過程中的星曆穩定性，減少長週期數值漂移。注意： 本工具完全基於數據驅動 (Data-driven)。所有修正參數均來自對觀測數據的統計擬合與算法優化。技術規格特性 / 參數規格描述應用目的臨界閾值 ($a_0$)$1.21 \times 10^{-10} \text{ m/s}^2$定義引力修正的物理邊界校正邏輯$a_{jct} = a_n \cdot (1 + \sqrt{a_0/a_n})$對齊 RAR (徑向加速度關係)計算核心原生 C 語言 (O3 優化)支持大規模 ($N > 10^5$) 質點模擬精度控制雙精度浮點數 (Double)降低長週期軌道的數值漂移開發與免責聲明開發註記：本 SDK 採用 AI 輔助編寫，以優化 C 語言核心效能與 Python 接口調用。免責聲明：本專案為私人獨立開發，代碼與數據僅供參考。作者不對結果正確性做任何保證。Maintained by Jinyan. Released under MIT License.
