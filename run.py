import numpy as np
import cv2 
from pathlib import Path
import logging
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def process_image(img_path):
    img = cv2.imread(str(img_path))
    if img is None:
        logger.error(f"Failed to read {img_path}")
        return None
    
    mask = np.all(img > 200, axis=2).astype(np.uint8) * 255
    out_path = Path("output") / f"{img_path.stem}_mask.png"
    cv2.imwrite(str(out_path), mask)
    
    return str(out_path), np.sum(mask == 255)

def main():
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    log_file = output_dir / f"processing_{datetime.now():%Y%m%d_%H%M}.txt"
    file_handler = logging.FileHandler(log_file)
    logger.addHandler(file_handler)
    
    input_dir = Path("images")
    images = list(input_dir.glob("*.jpg"))
    
    if not images:
        logger.warning("No JPG files found!")
        return
    
    logger.info(f"Processing {len(images)} images")
    
    # Process images in parallel
    results = []
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_image, img) for img in images]
        results = [f.result() for f in futures]
    
    # Filter out failed images and sum up white pixels
    successful = []
    total_white = 0

    for result in results:
        if result is not None:
            successful.append(result)
            _, white_pixels = result
            total_white += white_pixels
    
    # Summary
    logger.info(f"\nProcessed {len(successful)}/{len(images)} images")
    logger.info(f"Total white pixels: {total_white:,}")
    logger.info(f"Log saved to: {log_file}")

if __name__ == "__main__":
    main()