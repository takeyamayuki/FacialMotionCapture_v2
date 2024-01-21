import cv2

deviceid=1 # it depends on the order of USB connection. 
capture = cv2.VideoCapture(deviceid)

def job():
    ret, image = capture.read()
    if ret == False:
        print('cannot read image!')
        return
    # Show camera image in a window                     
    cv2.imshow("Output", image)
    cv2.waitKey(1)

def main():
    while True:
        job()

if __name__ == '__main__':
    main()