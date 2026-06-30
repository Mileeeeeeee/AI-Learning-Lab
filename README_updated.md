# 🧠 OpenCV Learning Journey (Day1 - Day6)

本项目记录从 OpenCV 入门 → 传统视觉检测 → 类 YOLO目标检测的完整学习路径。

---

# 📅 Day1：环境搭建 & 基础认知

## 🎯 学习目标
- 搭建 Ubuntu + WSL + VS Code + Python 环境
- 理解 OpenCV / Python / Linux 基础关系

## 🧰 环境工具
- Ubuntu (WSL2)
- VS Code + Remote WSL
- Python 3.12
- pip / uv（包管理）

## 📌 核心命令
```bash
python3 --version
which python3
pip3 list
```

## 🧠 核心认知
- Linux 是开发环境基础
- Python 是算法载体
- OpenCV 是视觉工具库

---

# 📅 Day2：Git & 项目管理

## 🎯 学习目标
- 掌握 Git 基础流程
- 建立 GitHub 仓库

## 📌 Git流程
```bash
git init
git add .
git commit -m "Day2 first commit"
git remote add origin <repo>
git push -u origin master
```

## 🧠 核心认知
- Git = 版本管理
- commit = 学习节点
- push = 云端备份

---

# 📅 Day3：虚拟环境 & uv工具

## 🎯 学习目标
- 使用 uv 管理 Python 环境
- 理解依赖隔离

## 📌 uv使用
```bash
uv init
uv add numpy
uv pip list
```

## ⚠️ 网络问题处理
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 🧠 核心认知
- 虚拟环境 = 项目隔离
- uv = 更快的 pip 替代方案

---

# 📅 Day4：OpenCV基础（图像处理）

## 🎯 学习目标
- 图像读取
- 灰度转换
- Canny边缘检测
- 图像拼接

## 📌 核心代码
```python
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
```

## 📊 图像处理流程
```
原图 → 灰度 → 边缘 → 可视化
```

## ⚠️ 问题总结
- Canny对噪声敏感
- 边缘断裂问题

---

# 📅 Day5：形态学操作 Morphology

## 🎯 学习目标
- 腐蚀 erosion
- 膨胀 dilation
- 开运算 / 闭运算

## 📌 核心逻辑

### 腐蚀
去除白色区域（缩小目标）

### 膨胀
扩展白色区域（增强目标）

## 📌 核心代码
```python
kernel = np.ones((3,3), np.uint8)

eroded = cv2.erode(img, kernel)
dilated = cv2.dilate(img, kernel)
```

## 🧠 核心认知
- Morphology = 结构处理
- 用于去噪 + 连通区域

---

# 📅 Day6：Contours & 目标检测雏形

## 🎯 学习目标
- Contours提取
- 目标筛选
- 简易检测系统

---

## 📌 标准流程

```
原图
 ↓
灰度
 ↓
高斯模糊
 ↓
二值化（OTSU）
 ↓
形态学去噪
 ↓
Contours
 ↓
目标筛选
 ↓
Bounding Box
```

---

## 📌 Contour提取

```python
contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

---

## 📌 目标筛选规则

### 面积过滤
```python
if area < 1000:
    continue
```

### 长宽比过滤
```python
aspect = w / float(h)

if aspect < 0.2 or aspect > 5:
    continue
```

---

## 📌 YOLO-lite思想（重要）

### 传统CV
if/else 规则过滤

### YOLO思想
候选 → 打分 → 排序 → 输出

---

## 📌 评分系统（核心升级）

```python
score = area / 1000

if 0.5 < aspect < 2.5:
    score += 5
```

---

## 📌 输出结构（类YOLO）

```json
{
  "bbox": [x, y, w, h],
  "score": 8.2
}
```

---

## 📌 最终能力

- 自动检测目标
- 自动筛选噪声
- 输出检测结果
- 可视化 bounding box

---

# 🚀 学习阶段总结

Day1  环境搭建  
Day2  Git管理  
Day3  环境隔离  
Day4  图像处理  
Day5  形态学  
Day6  目标检测雏形  

---

# 🧠 核心认知升级

## ❌ 初级
OpenCV = 图像处理函数

## ✅ 当前
OpenCV = 目标检测工具链

---

# 🚀 下一阶段（Day7+）

## Day7：IoU + NMS
## Day8：检测系统优化
## Day9：YOLO思想深化


---

# 📅 Day7：IoU & NMS（检测系统核心）

## 🎯 学习目标
- 理解 IoU（交并比）
- 理解 NMS（非极大值抑制）
- 优化检测框去重逻辑

## 🧠 核心理论

### 📌 IoU（Intersection over Union）
用于衡量两个框的重叠程度：

IoU = 交集 / 并集

### 📌 NMS思想
1. 按 score 排序
2. 选最高分框
3. 删除 IoU > 阈值的重复框
4. 重复直到结束

## 🚀 工程意义
- 去除重复检测框
- 提升检测稳定性
- YOLO核心组件之一

---

# 📅 Day8：Region Proposal（候选区域生成）

## 🎯 学习目标
- 理解候选区域思想
- 从 contour → region proposal
- 理解检测系统上游结构

## 🧠 核心理论

### 📌 核心思想
先“找可能有目标的区域”，再分类/评分

### 📌 方法
- Sliding Window（穷举）
- Grid Proposal（当前实现）
- Selective Search（进阶）

## 📌 工程意义
- 替代 edge/contour 依赖
- 提高鲁棒性
- 降低背景敏感性

---

# 📅 Day9：Feature-based Detection（特征检测）

## 🎯 学习目标
- 引入特征描述思想
- 替代纯规则 scoring
- 初步接近 ML 检测

## 🧠 核心理论

### 📌 Feature思想
不直接看像素，而看统计特征：

- 颜色分布（HSV histogram）
- 纹理（LBP）
- 梯度（HOG简化）

### 📌 scoring升级
score = f(color, texture, shape)

## 🚀 工程意义
- 从 rule-based → feature-based
- 为 YOLO/CNN铺垫

---

# 🧠 学习方法升级（重要）

从 Day7 开始统一结构：

## 每一课包含：
1. 🎯 目标
2. 🧠 理论
3. 📌 核心算法
4. 🚀 工程实现
5. 📚 参考资料（论文/关键词）

---

# 🚀 总体学习路线（更新版）

Day1-6  OpenCV基础  
Day7     IoU + NMS  
Day8     Region Proposal  
Day9     Feature-based Detection  
Day10+   YOLO / Deep Learning Detection  

