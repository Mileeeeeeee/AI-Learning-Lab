# AI工程师成长计划学习笔记（Day1-Day3）

## 学习目标
方向：机器视觉、自动驾驶、机器人、产品工程、系统工程、创业

硬件：
- Windows 11
- i5-1035G1
- 16GB RAM
- MX350
- 500GB SSD

---

# Day1：开发环境搭建

## 目标
建立 Linux + VS Code 开发环境。

## 完成内容
### WSL2 安装
验证：

```bash
wsl --status
```

安装：

```bash
wsl --install Ubuntu-24.04
```

### Ubuntu 使用

进入 Linux：

```bash
wsl
```

切换到用户目录：

```bash
cd ~
pwd
```

### 学习目录规划

E盘目录：

```text
E:\AI_Learning
```

Linux映射：

```bash
cd /mnt/e/AI_Learning
```

目录结构：

```text
AI_Learning
├── Linux
├── Git
├── OpenCV
├── YOLO
├── ROS2
├── Projects
├── Dataset
├── Models
├── Videos
└── Notes
```

### VS Code + WSL

打开当前目录：

```bash
code .
```

安装插件：

- WSL
- Python
- Pylance
- Python Debugger

---

# Day2：Git 与 GitHub

## 目标
建立工程化代码管理能力。

### Git基础

查看版本：

```bash
git --version
```

初始化仓库：

```bash
git init
```

查看状态：

```bash
git status
```

### 第一次提交

```bash
git add .
git commit -m "Day2:first commit"
```

### GitHub SSH

生成密钥：

```bash
ssh-keygen -t ed25519 -C "Mileeeeeeee@github"
```

测试连接：

```bash
ssh -T git@github.com
```

成功标志：

```text
Hi Mileeeeeeee!
You've successfully authenticated
```

### 远程仓库

仓库：

AI-Learning-Lab

添加远程仓库：

```bash
git remote add origin git@github.com:Mileeeeeeee/AI-Learning-Lab.git
```

查看：

```bash
git remote -v
```

### 第一次Push

```bash
git push -u origin master
```

### Git日常命令

```bash
git status
git add .
git commit -m "message"
git push
git pull
git log --oneline
```

---

# Day3：Python工程化

## 目标
建立现代Python项目开发流程。

## uv安装

安装：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

激活：

```bash
source $HOME/.local/bin/env
```

验证：

```bash
uv --version
```

## 配置清华镜像

文件：

```bash
~/.config/uv/uv.toml
```

内容：

```toml
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
```

## 创建项目

```bash
mkdir Python
cd Python

uv init Day3_Python
cd Day3_Python
```

## 创建虚拟环境

```bash
uv venv
source .venv/bin/activate
```

## 安装依赖

```bash
uv add numpy
```

查看：

```bash
uv pip list
```

## 第一个程序

hello_ai.py

```python
import numpy as np

data = np.array([1,2,3,4,5])

print("Hello AI Engineer")
print("Array:", data)
print("Mean:", data.mean())
print("Max:", data.max())
print("Min:", data.min())
```

运行：

```bash
python hello_ai.py
```

输出：

```text
Hello AI Engineer
Array: [1 2 3 4 5]
Mean: 3.0
Max: 5
Min: 1
```

## Git提交

```bash
git add .
git commit -m "Add Day3 Python uv project"
git push
```

---

# 当前能力评估

已掌握：

- Linux基础
- WSL2
- VS Code远程开发
- Git
- GitHub
- SSH
- Python工程化
- uv
- NumPy

---

# Day4目标

OpenCV机器视觉入门：

1. OpenCV安装
2. 图像读取
3. 图像显示
4. 灰度化
5. 边缘检测
6. 摄像头读取
7. AI辅助视觉编程

---

# 长期路线图

第1周：Linux + Git + Python

第2周：OpenCV

第3周：YOLO目标检测

第4周：ROS2 + 机器人视觉

项目：

- AI视觉检测系统
- 智能巡检机器人
- 自动驾驶小车
