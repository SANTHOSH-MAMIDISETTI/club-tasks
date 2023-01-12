import cv2
import pytesseract as pt
img = cv2.imread('task-2\img3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary Image", thresh)
text = pt.image_to_string(thresh , lang='eng+equ',config='--psm 12 --oem 3 -c tessedit_char_whitelist=0123456789+-=?')
print("captcha is ",text)
if text == '':
    print("No text found")
elif text != '':
    if text.find('=') != '':
        nt=text.replace('=','')
        nnt=nt.replace('?','')
        print(eval(nnt))
else:print("No '=' found")

# 1 3 4    5 =+  6  11  12

# cap1 ; img 4 ; img 5