from array import array
from load_image import ft_load
import copy
import cv2


def ft_invert(array) -> array:
    """def ft_invert(array)"""
    ret = copy.deepcopy(array)
    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            ret[y, x, 0] = 255 - array[y, x, 0]
            ret[y, x, 1] = 255 - array[y, x, 1]
            ret[y, x, 2] = 255 - array[y, x, 2]
    return (ret)


def ft_red(array) -> array:
    """def ft_red(array)"""
    ret = copy.deepcopy(array)
    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            ret[y, x, 0] = 0
            ret[y, x, 1] = 0
    return (ret)


def ft_green(array) -> array:
    """def ft_green(array)"""
    ret = copy.deepcopy(array)
    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            ret[y, x, 0] = 0
            ret[y, x, 2] = 0
    return (ret)


def ft_blue(array) -> array:
    """def ft_blue(array)"""
    ret = copy.deepcopy(array)
    for x in range(array.shape[1]):
        for y in range(array.shape[0]):
            ret[y, x, 1] = 0
            ret[y, x, 2] = 0
    return (ret)


def ft_grey(array) -> array:
    """def ft_grey(array)"""
    return (cv2.cvtColor(array, cv2.COLOR_BGR2GRAY))


def main():
    # Load the image
    img = ft_load("landscape.jpg")
    img_invert = ft_invert(img)
    img_red = ft_red(img)
    img_green = ft_green(img)
    img_blue = ft_blue(img)
    img_gray = ft_grey(img)

    # Display the image in a window
    cv2.imshow("Landscape", img)
    cv2.imshow("Invert", img_invert)
    cv2.imshow("Red", img_red)
    cv2.imshow("Green", img_green)
    cv2.imshow("Blue", img_blue)
    cv2.imshow("Gray", img_gray)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
