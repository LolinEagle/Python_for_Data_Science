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
    return (cv2.imread(path))
