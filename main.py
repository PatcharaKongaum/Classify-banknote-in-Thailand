import cv2
import tkinter as tk
from gtts import gTTS
import os

blue_lower = (90, 50, 50)
blue_upper = (130, 255, 255)

purple_lower = (120, 50, 50)
purple_upper = (160, 255, 255)

red_lower1 = (0, 50, 50)
red_upper1 = (10, 255, 255)
red_lower2 = (160, 50, 50)
red_upper2 = (180, 255, 255)

yellow_lower = (20, 50, 50)
yellow_upper = (35, 255, 255)

green_lower = (35, 50, 50)
green_upper = (85, 255, 255)

def display_color_results(green_pixel_count, blue_pixel_count, purple_pixel_count, red_pixel_count, yellow_pixel_count):
    root = tk.Tk()
    root.title("Results")
    color_result = f"สีที่ตรวจจับได้\nเขียว: {green_pixel_count}\nน้ำเงิน: {blue_pixel_count}\nม่วง: {purple_pixel_count}\nแดง: {red_pixel_count}\nเหลือง: {yellow_pixel_count}"
    color_label = tk.Label(root, text=color_result, font=("TH Sarabun New", 32))
    color_label.pack()
    os.system("start sound.wav")
    root.after(1000, root.destroy)

    root.mainloop()

def capture_and_detect_color():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    cv2.imwrite("captured_image.jpg", frame)

    cap.release()

    detect_color_from_image('captured_image.jpg')

def detect_color_from_image(image_path):
    image = cv2.imread(image_path)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv_image, blue_lower, blue_upper)
    mask_purple = cv2.inRange(hsv_image, purple_lower, purple_upper)
    mask_red1 = cv2.inRange(hsv_image, red_lower1, red_upper1)
    mask_red2 = cv2.inRange(hsv_image, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_yellow = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    mask_green = cv2.inRange(hsv_image, green_lower, green_upper)

    blue_pixel_count = cv2.countNonZero(mask_blue)
    purple_pixel_count = cv2.countNonZero(mask_purple)
    red_pixel_count = cv2.countNonZero(mask_red)
    yellow_pixel_count = cv2.countNonZero(mask_yellow)
    green_pixel_count = cv2.countNonZero(mask_green)

    threshold = 1000
    if green_pixel_count >= threshold:
        text_to_speak = "20 บาท"
        print("20")
    elif red_pixel_count >= threshold:
        text_to_speak = "100 บาท"
        print("100")
    elif blue_pixel_count >= threshold:
        text_to_speak = "50 บาท"
        print("50")
    elif purple_pixel_count >= threshold:
        text_to_speak = "500 บาท"
        print("500")
    elif yellow_pixel_count >= threshold:
        text_to_speak = "1000 บาท"
        print("1000")
    else:
        print("Error : Validation conditions not found.")
        text_to_speak = "Error : Validation conditions not found. ไม่พบรูปที่ตรงกับเงื่อนไข"

    display_color_results(green_pixel_count, blue_pixel_count, purple_pixel_count, red_pixel_count, yellow_pixel_count)

    tts = gTTS(text=text_to_speak, lang='th')
    tts.save("output.mp3")
    os.system("start output.mp3")

# เริ่มต้นโปรแกรม
capture_and_detect_color()
