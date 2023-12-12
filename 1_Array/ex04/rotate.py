from load_image import ft_load
import copy
import cv2


def main():
    # Load the image
    img = ft_load("animal.jpeg")
    if (img.shape[0] < 400 or img.shape[1] < 400):
        print("Image not big enough")
        return (0)

    # Convert the color image to grayscale image
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Convert the grayscale image to zoomed image
    x1 = int(img_gray.shape[1] / 2) - 200
    x2 = int(img_gray.shape[1] / 2) + 200
    y1 = int(img_gray.shape[0] / 2) - 200
    y2 = int(img_gray.shape[0] / 2) + 200
    img_zoom = img_gray[y1:y2, x1:x2]

    # Convert the zoomed image to rotated image
    img_rotate = copy.deepcopy(img_zoom)
    for x in range(400):
        for y in range(400):
            img_rotate[y, x] = img_zoom[x, y]

    # Print
    print(f"The shape of image is: ({img_zoom.shape[0]}, {img_zoom.shape[1]}, \
1) or {img_zoom.shape}")
    print(img_gray)
    print(f"New shape after Transpose: {img_rotate.shape}")
    print(img_rotate)

    # Display the image in a window
    cv2.imshow("", img_rotate)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
