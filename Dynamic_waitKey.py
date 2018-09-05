import cv2
url = 'sample.jpg'
img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Title',img)
waitingTime = input("Enter waiting time in millisecs : ")
cv2.waitKey(waitingTime)
cv2.destroyAllWindows()

#Note : Image window closes after 'ip' millisecs or until a key is pressed by the user externally.
