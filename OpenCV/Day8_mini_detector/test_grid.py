import cv2
import config as cfg

from proposals.grid import GridProposal
from utils.run_manager import RunManager


def draw_grid(image, proposals, step):

    vis = image.copy()

    h, w = image.shape[:2]

    for (x, y, bw, bh) in proposals:
        cv2.rectangle(vis,
                      (x, y),
                      (x + bw, y + bh),
                      (0, 255, 0), 1)

    for y in range(0, h, step):
        cv2.line(vis, (0, y), (w, y), (255, 0, 0), 1)

    for x in range(0, w, step):
        cv2.line(vis, (x, 0), (x, h), (255, 0, 0), 1)

    return vis


def main():

    # =====================
    # 1. Run Manager
    # =====================
    run = RunManager(cfg.OUTPUT_DIR)

    # =====================
    # 2. Load Image
    # =====================
    img = cv2.imread(cfg.IMAGE_PATH)

    # =====================
    # 3. Proposal
    # =====================
    generator = GridProposal(step=cfg.GRID_STEP)
    proposals = generator.generate(img)

    print("[INFO] proposals:", len(proposals))

    # =====================
    # 4. Visualize
    # =====================
    vis = draw_grid(img, proposals, cfg.GRID_STEP)

    # =====================
    # 5. Save (run isolated)
    # =====================
    run.save_image(f"grid_step_{cfg.GRID_STEP}.jpg", vis)



if __name__ == "__main__":
    main()