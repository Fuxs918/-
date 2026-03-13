# 智能扫码器 - Android APK 构建指南

这是一个基于Kivy框架开发的智能扫码应用，包含以下功能：
- 实时摄像头扫码
- 扫码记录管理
- 分组管理
- 连号设置
- Excel导出

## 文件清单
- `main.py`: 主程序代码
- `buildozer.spec`: Buildozer配置文件
- `icon.png`: 应用图标
- `assets/`: 资源文件目录

## 构建步骤

### 方法一：使用Buildozer（推荐）

1. 安装必要的依赖：
```bash
sudo apt update
sudo apt install -y build-essential git python3 python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

2. 安装Buildozer：
```bash
pip3 install --user --upgrade buildozer
```

3. 在项目根目录运行构建命令：
```bash
cd /path/to/your/project
buildozer android debug
```

生成的APK文件将在 `bin` 目录下。

### 方法二：使用Python-for-Android直接构建

1. 安装python-for-android：
```bash
pip3 install python-for-android
```

2. 构建APK：
```bash
p4a apk --private . --package=org.example.smartscanner --name="智能扫码器" --version=1.0 --bootstrap=sdl2 --requirements=python3,kivy==2.0.0,pillow,openpyxl,pyzbar,opencv-python,jnius,plyer --arch=armeabi-v7a --copy-libs
```

## 权限说明
本应用需要以下权限：
- CAMERA: 用于扫码功能
- VIBRATE: 用于扫码震动反馈
- FLASHLIGHT: 控制手电筒
- WRITE_EXTERNAL_STORAGE/READ_EXTERNAL_STORAGE: 导出Excel文件

## 注意事项
1. 构建过程可能需要较长时间，请耐心等待。
2. 首次构建会下载大量依赖项，确保网络连接稳定。
3. 如果遇到问题，可以查看Buildozer日志以获取更多信息。
4. 为了获得最佳性能，建议在Linux系统上进行构建。

## 故障排除
如果构建失败，请尝试：
1. 更新所有包到最新版本
2. 清理之前的构建缓存：`buildozer android clean`
3. 确保有足够的磁盘空间（至少2GB可用）
4. 检查Java和SDK环境是否正确安装

## 开发者信息
此项目由AI助手为您创建，如有疑问请联系技术支持。
