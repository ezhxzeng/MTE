from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects


def display(im, decodedObjects):
    '''
    :param im: image
    :param decodedObjects: pyzbar.decode results
    :return: list of bounding coordinates
    also prints qr code bounding box
    '''
    points = []
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        rect = decodedObject.rect

        current_points = [(rect[0], rect[1]), (rect[0] + rect[2], rect[1]),
                          (rect[0] + rect[2], rect[1] + rect[3]), (rect[0], rect[1] + rect[3])]
        points.append(current_points)

        # Number of points in the convex hull
        n = len(current_points)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, current_points[j], current_points[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)
    cv2.waitKey(0)
    return points


# Main
if __name__ == '__main__':
    # Read image
    im = cv2.imread('test_qr_code.PNG')

    decodedObjects = decode(im)
    points = display(im, decodedObjects)
