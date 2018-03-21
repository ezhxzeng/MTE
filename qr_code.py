from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2


def decode(im):
    '''
    :param im: cv2.imread results
    :return: pyzar.decode results, [{data, width, height}]
    '''
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    if len(decodedObjects) >1:
        return decodedObjects, {0}

    print('Type : ', decodedObjects[0].type)
    print('Data : ', decodedObjects[0].data, '\n')

    rect = decodedObjects[0].rect
    qr_info = {"data": int(decodedObjects[0].data), "width": rect.width,
               "height": rect.height, "points": [(rect[0], rect[1]), (rect[0] + rect[2], rect[1]),
                                                 (rect[0] + rect[2], rect[1] + rect[3]),
                                                 (rect[0], rect[1] + rect[3])]}

    return decodedObjects, qr_info


def display(im, decodedObjects):
    '''
    :param im: image
    :param decodedObjects: pyzbar.decode results
    prints qr code bounding box
    '''
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        rect = decodedObject.rect
        print(decodedObject)

        points = [(rect[0], rect[1]), (rect[0] + rect[2], rect[1]),
                  (rect[0] + rect[2], rect[1] + rect[3]), (rect[0], rect[1] + rect[3])]

        # Number of points in the convex hull
        n = len(points)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, points[j], points[(j + 1) % n], (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)
    cv2.waitKey(0)
    return


# Main
if __name__ == '__main__':
    # Read image
    im = cv2.imread('test_qr_code.PNG')

    decodedObjects, qr_info = decode(im)
    display(im, decodedObjects)
    print(qr_info)
