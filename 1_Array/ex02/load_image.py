import imageio.v2 as iio
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
    img = iio.imread(path)
    print(f"The shape of image is: {img.shape}")
    return (img)


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
