#!/bin/bash

# 智能扫码器 APK 构建脚本
# 请在Linux或Mac系统上运行此脚本

echo "开始构建智能扫码器 APK..."

# 检查是否安装了必要的工具
if ! command -v python3 &>/dev/null; then
    echo "错误: 未找到python3，请先安装Python 3"
    exit 1
fi

if ! command -v pip3 &>/dev/null; then
    echo "警告: 未找到pip3，尝试安装..."
    sudo apt update && sudo apt install python3-pip
fi

# 安装Buildozer
echo "正在安装Buildozer..."
pip3 install --user buildozer

# 初始化Buildozer（如果需要）
if [ ! -d ".buildozer" ]; then
    echo "初始化Buildozer..."
    buildozer init
fi

# 更新spec文件中的路径和依赖
SPEC_FILE="buildozer.spec"

# 确保spec文件存在
if [ ! -f "$SPEC_FILE" ]; then
    echo "错误: 找不到buildozer.spec文件"
    exit 1
fi

echo "开始构建APK..."
echo "这可能需要几分钟时间，请耐心等待..."

# 构建调试版APK
buildozer android debug

echo "构建完成！"
echo "APK文件位于 bin/ 目录下"
echo ""
echo "如果构建失败，请尝试以下步骤："
echo "1. 运行 'buildozer android clean' 清理缓存"
echo "2. 确保已安装Java JDK"
echo "3. 确保网络连接稳定"
echo "4. 检查是否有足够的磁盘空间"
