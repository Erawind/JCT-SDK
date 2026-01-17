#!/bin/bash

echo "🚀 JCT Engine Compiler Starting..."

# 檢查是否有安裝 gcc
if ! command -v gcc &> /dev/null
then
    echo "❌ Error: 'gcc' not found. Please install a C compiler."
    exit
fi

# 編譯 C 核心引擎 (Linux/macOS)
echo "📦 Compiling jct_engine.c into jct_engine.so..."
gcc -O3 -shared -fPIC -o jct_engine.so jct_engine.c -lm

if [ $? -eq 0 ]; then
    echo "✅ Success! 'jct_engine.so' is ready."
    echo "💡 You can now run your Python code using jct_wrapper.py."
else
    echo "❌ Compilation failed. Please check for errors in jct_engine.c."
fi
