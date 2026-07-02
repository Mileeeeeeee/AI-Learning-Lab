import os
import cv2
from datetime import datetime


class RunManager:

    def __init__(self, base_dir="results"):

        self.base_dir = base_dir

        # run_id
        self.run_id = datetime.now().strftime("run_%Y%m%d_%H%M%S")

        # run path
        self.run_path = os.path.join(base_dir, self.run_id)

        self._init_dirs()

        print(f"[RUN] {self.run_id}")

    # =========================
    # 初始化目录
    # =========================
    def _init_dirs(self):

        os.makedirs(self.run_path, exist_ok=True)

    # =========================
    # 获取路径
    # =========================
    def get_path(self, filename):

        return os.path.join(self.run_path, filename)

    # =========================
    # 保存图片
    # =========================
    def save_image(self, filename, image):

        save_path = self.get_path(filename)

        # 如果传入 None（比如log占位）
        if image is None:
            with open(save_path, "w") as f:
                f.write("")
        else:
            cv2.imwrite(save_path, image)

        print(f"[SAVE] {save_path}")

        return save_path