import os
import cv2
import numpy as np


def preprocess(image_path):
    """
    读取图像并完成灰度化、二值化
    """
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError(f"Cannot find {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, binary = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return img, gray, binary


def morphology(binary):
    """
    形态学处理
    """
    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(binary, kernel, iterations=1)

    dilation = cv2.dilate(binary, kernel, iterations=1)

    opening = cv2.morphologyEx(
        binary,
        cv2.MORPH_OPEN,
        kernel
    )

    closing = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel
    )

    return erosion, dilation, opening, closing


def to_bgr(image):
    """
    灰度图转换成BGR，方便拼接
    """
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image


def save_images(result_dir,
                binary,
                erosion,
                dilation,
                opening,
                closing):
    """
    保存各个结果
    """

    cv2.imwrite(os.path.join(result_dir, "binary.jpg"), binary)
    cv2.imwrite(os.path.join(result_dir, "erosion.jpg"), erosion)
    cv2.imwrite(os.path.join(result_dir, "dilation.jpg"), dilation)
    cv2.imwrite(os.path.join(result_dir, "opening.jpg"), opening)
    cv2.imwrite(os.path.join(result_dir, "closing.jpg"), closing)


def add_title(img, title):
    """
    在图片左上角添加标题
    """
    image = img.copy()

    cv2.putText(
        image,
        title,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    return image


def main():

    image_path = "images/test.jpg"
    result_dir = "results"

    os.makedirs(result_dir, exist_ok=True)

    # ---------------------------
    # 图像预处理
    # ---------------------------
    original, gray, binary = preprocess(image_path)

    # ---------------------------
    # 形态学处理
    # ---------------------------
    erosion, dilation, opening, closing = morphology(binary)

    # ---------------------------
    # 保存单张图片
    # ---------------------------
    save_images(
        result_dir,
        binary,
        erosion,
        dilation,
        opening,
        closing
    )

    # ---------------------------
    # 转换为BGR
    # ---------------------------
    gray = to_bgr(gray)
    binary = to_bgr(binary)
    erosion = to_bgr(erosion)
    dilation = to_bgr(dilation)
    opening = to_bgr(opening)
    closing = to_bgr(closing)

    # ---------------------------
    # 添加标题
    # ---------------------------
    original = add_title(original, "Original")
    binary = add_title(binary, "Binary")
    erosion = add_title(erosion, "Erosion")
    dilation = add_title(dilation, "Dilation")
    opening = add_title(opening, "Opening")
    closing = add_title(closing, "Closing")

    # ---------------------------
    # 第一行
    # ---------------------------
    row1 = cv2.hconcat([
        original,
        binary,
        erosion
    ])

    # ---------------------------
    # 第二行
    # ---------------------------
    row2 = cv2.hconcat([
        dilation,
        opening,
        closing
    ])

    compare = cv2.vconcat([
        row1,
        row2
    ])

    cv2.imwrite(
        os.path.join(result_dir, "morphology_compare.jpg"),
        compare
    )

    print("=" * 40)
    print("Morphology Demo Finished!")
    print("Results saved in ./results/")
    print("=" * 40)


if __name__ == "__main__":
    main()