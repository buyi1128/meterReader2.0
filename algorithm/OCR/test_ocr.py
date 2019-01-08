import cv2
from utils import *

svc = svmOCR()
net = leNetOCR()

for i in range(10):
    image = cv2.imread("bin/"+str(i)+".jpg", cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))

    ret, binary = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
    binary = binary

    cv2.imshow("digit", binary)
    cv2.waitKey(500)

    numSvm = svc.recognizeSvm(binary)
    numNet = net.recognizeNet(binary)

    print(i, "\tsvm:", numSvm, "\tLeNet", numNet)
    print(i, "\tsvm:", numSvm, "\tLeNet", numNet)