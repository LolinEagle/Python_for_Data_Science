import cv2
import os


def ft_load(path: str):
    """def ft_load(path: str)"""
    try:
        if not (os.path.exists(path)):
            raise FileNotFoundError("File not found")
        if not (os.access(path, os.R_OK)):
            raise PermissionError("Permission denied")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return
    img = cv2.imread(path)
    print(f"The shape of image is: {img.shape}")
    return (cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
