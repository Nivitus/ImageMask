# ImageMask
This code creates binary mask images from JPG photos using OpenCV. Masks highlight pixels where all color channels exceed 200. The masks are saved as lossless files, and the total count of qualifying pixels across all images is logged for analysis. Efficient and easy to use!

## Features

- Process multiple images in parallel using available CPU cores
- Create binary masks for images (threshold > 200)
- Count white pixels in each image
- Generate detailed processing logs
- Support for JPG images
- Automated output directory creation

## Requirements

```python
numpy==1.24.3
opencv-python==4.8.0
```
## Installation

#### 1. Clone the repository:
```
git clone https://github.com/Nivitus/ImageMask.git
cd ImageMask
```

#### 2. Install required packages:
```
pip3 install -r requirements.txt
```

#### 3. Run the Script
```
python3 run.py
```


