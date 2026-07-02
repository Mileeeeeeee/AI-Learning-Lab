# config.py

import os

# =====================
# 输入输出路径
# =====================
IMAGE_PATH = "images/test.jpg"
OUTPUT_DIR = "results"

# 自动创建输出目录
os.makedirs(OUTPUT_DIR, exist_ok=True)

GRID_STEP = 80

# =====================
# preprocess params
# =====================
CANNY_LOW = 120
CANNY_HIGH = 240

BLUR_K1 = 5
BLUR_K2 = 5

# =====================
# detection params
# =====================
MIN_AREA = 1000

ASPECT_MIN = 0.7
ASPECT_MAX = 2.0

# =====================
# scoring
# =====================
SCORE_AREA_DIV = 1000

# =====================
# NMS
# =====================
NMS_IOU_THRESH = 0.5


