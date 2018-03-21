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

    # qr_info = []
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')
        qr_info = {"data": obj.data, "width": obj.rect.width, "height": obj.rect.height}

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
        print (decodedObject)

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
