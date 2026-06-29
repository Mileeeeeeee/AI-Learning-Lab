# Day4–Day5 OpenCV学习总结

## 📌 Day4：图像基础 + 边缘检测

### 🎯 学习目标
- 理解图像在计算机中的本质（矩阵）
- 掌握 OpenCV 基础处理流程
- 理解 Canny 边缘检测原理
- 建立“图像 = 数字信号”的认知

### 🧠 核心知识

图像是 H×W×C 的矩阵（BGR三通道）

Canny流程：
GaussianBlur → Sobel → 非极大值抑制 → 双阈值

### ⚠️ 常见问题
- 阈值过高：边缘断裂
- 阈值过低：噪声过多

---

## 📌 Day5：形态学处理（Morphology）

### 🎯 学习目标
- 二值化
- 腐蚀/膨胀
- Opening / Closing
- 工业预处理流程

---

## 🧠 核心概念

Threshold：0或255二值图

Kernel：局部邻域操作窗口

Erosion：收缩白色区域（最小值）

Dilation：扩张白色区域（最大值）

---

## 🔁 Opening
Erosion → Dilation（去白噪声）

## 🔁 Closing
Dilation → Erosion（填黑洞）

---

## 📊 工业结论
- Opening：去噪
- Closing：补洞
- Kernel越大效果越强但可能破坏结构

---

## 🚀 总结
Day4：理解边缘（变化率）
Day5：控制结构（形态学变换）
