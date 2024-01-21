# These codes were solely written by MATTHEW NG WEI CHEN during the Hack&Roll 2024 hackathon, which was graciously organised by NUS Hackers!
# I deeply thank their team for giving me this wonderful opportunity to showcase my passion project. The event really means a lot to me.
# Also, if you are referencing my work, please credit me:
# GitHub : @MatthewYay
# LinkedIn : https://www.linkedin.com/in/matthew-ng-wc/

import cv2
import mediapipe as mp
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
webcamRecording = cv2.VideoCapture(0)
webcamRecording.set(8, 200000)
webcamRecording.set(9, 200000)
firstPicture = cv2.imread('emPetAIze_pictures/greenMagicRings.png', -1)
secondPicture = cv2.imread('emPetAIze_pictures/iLoveYou.png', -1)
degree = 0
gameRoot = tk.Tk()
gameRoot.title("Empetaize (Game)")
photo = tk.PhotoImage(file='emPetAIze_pictures/catTkinterMainIcon.png')
gameRoot.iconphoto(False, photo)
tkinterWidth = gameRoot.winfo_screenwidth()
tkinterHeight = gameRoot.winfo_screenheight()
#gameRoot.geometry("%dx%d" % (tkinterWidth, tkinterHeight))
gameRoot.geometry(
    f'{tkinterWidth}x{tkinterHeight}+{(int((tkinterWidth/2)-(tkinterWidth/2)))-8}+{int((tkinterHeight/2)-(tkinterHeight/2))-5}')
gameRoot.minsize(tkinterWidth, tkinterHeight)
gameRoot.maxsize(tkinterWidth, tkinterHeight)
gameRoot.configure(bg="#270f36")
gameRoot.resizable(False, False)
canvasHeight = tkinterHeight / 5 * 4
canvasWidth = canvasHeight / 3 * 4
canvas = tk.Canvas(gameRoot, bg="#270f36", width=canvasWidth, height=canvasHeight)
labelEmpty = tk.Label(gameRoot, text=" ", bg="#270f36", fg="white", font=("Arial", 1, "bold"))
labelOne = tk.Label(gameRoot, text="Raise Your Hand to See Something Special!", bg="#270f36", fg="yellow",
                    font=("Arial Black", 20, "bold"))
labelTwo = tk.Label(gameRoot, text=" ", bg="#270f36", fg="white", font=("Arial", 8, "bold"))
labelEmpty.pack()
labelOne.pack()
canvas.pack()
labelTwo.pack()
areThereHandsInWebcamVid = False

def return_to_homePage():
    global showAnimation
    if showAnimation is not None:
        gameRoot.after_cancel(showAnimation) # Cancel the animation
    gameRoot.destroy() # Hide the current window
    import home_page # Import the home_page module
    home_page.homeRoot # Show the home_page.py window

back_to_home_button_img = None

goBackHomeBtn = tk.Button(gameRoot, image=back_to_home_button_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=return_to_homePage)
goBackHomeBtn.place(x=20, y=20)
# goBackHomeBtn.transparency_set("#270f36")

def load_back_to_home_button():
    global back_to_home_button_img
    original_image = Image.open("emPetAIze_pictures/backToHomeScreenButton.png")
    resized_image = original_image.resize((153, 35))
    back_to_home_button_img = ImageTk.PhotoImage(resized_image)
    goBackHomeBtn.configure(image=back_to_home_button_img, compound=tk.LEFT)
    goBackHomeBtn.image = back_to_home_button_img

load_back_to_home_button()

originalPhoto = Image.open("emPetAIze_pictures/catInHat.png")
oriPhoto = ImageTk.PhotoImage(originalPhoto)
gif_label = Label(gameRoot, image=oriPhoto, bg="#270f36")
gif_label.place(x=tkinterWidth - 225, y=tkinterHeight - 350)
gifImage = "emPetAIze_pictures\\catLove.gif"
openImage = Image.open(gifImage)
frames = openImage.n_frames
imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
count = 0
showAnimation = None

def animation(count):
    global showAnimation
    global areThereHandsInWebcamVid
    newImage = imageObject[count]
    gif_label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    # Continue the animation if the hand landmarks are still detected
    if areThereHandsInWebcamVid:
        showAnimation = gameRoot.after(400, lambda: animation(count)) #Delay time, slows GIF
    # Otherwise, switch back to displaying catInHat.png
    else:
        gif_label.configure(image=oriPhoto)

def convert_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)
    return image

def draw_image(image):
    canvas.create_image(0, 0, anchor=tk.NW, image=image)

def position_data(lmlist):
    global wrist, thumb_tip, index_mcp, index_tip, midle_mcp, midle_tip, ring_tip, pinky_tip
    wrist = (lmlist[0][0], lmlist[0][1])
    thumb_tip = (lmlist[4][0], lmlist[4][1])
    index_mcp = (lmlist[5][0], lmlist[5][1])
    index_tip = (lmlist[8][0], lmlist[8][1])
    midle_mcp = (lmlist[9][0], lmlist[9][1])
    midle_tip = (lmlist[12][0], lmlist[12][1])
    ring_tip  = (lmlist[16][0], lmlist[16][1])
    pinky_tip = (lmlist[20][0], lmlist[20][1])

def draw_line(p1, p2, size=5):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill='black', width=size)

def calculate_distance(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return length

def transparent(targetImg, x, y, size=None):
    if size is not None:
        targetImg = cv2.resize(targetImg, size)
    newFrame = img.copy()
    b, g, r, a = cv2.split(targetImg)
    overlay_color = cv2.merge((b, g, r))
    mask = cv2.medianBlur(a, 1)
    h, w, _ = overlay_color.shape
    roi = newFrame[y:y + h, x:x + w]
    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return newFrame

while True:
    ret, img = webcamRecording.read()
    img = cv2.flip(img, 1)
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    img = cv2.resize(img, (canvas_width, canvas_height))
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgbimg)
    if result.multi_hand_landmarks:
        areThereHandsInWebcamVid = True
        for hand in result.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                coorx, coory = int(lm.x * w), int(lm.y * h)
                lmList.append([coorx, coory])

            position_data(lmList)
            palm = calculate_distance(wrist, index_mcp)
            distance = calculate_distance(index_tip, pinky_tip)
            ratio = distance / palm
            print(ratio)
            if 1.3 > ratio > 0.5:
                draw_line(wrist, thumb_tip)
                draw_line(wrist, index_tip)
                draw_line(wrist, midle_tip)
                draw_line(wrist, ring_tip)
                draw_line(wrist, pinky_tip)
                draw_line(thumb_tip, index_tip)
                draw_line(thumb_tip, midle_tip)
                draw_line(thumb_tip, ring_tip)
                draw_line(thumb_tip, pinky_tip)
            if ratio > 1.3:
                centerx = midle_mcp[0]
                centery = midle_mcp[1]
                shield_size = 3.0
                diameter = round(palm * shield_size)
                x1 = round(centerx - (diameter / 2))
                y1 = round(centery - (diameter / 2))
                h, w, c = img.shape
                if x1 < 0:
                    x1 = 0
                elif x1 > w:
                    x1 = w
                if y1 < 0:
                    y1 = 0
                elif y1 > h:
                    y1 = h
                if x1 + diameter > w:
                    diameter = w - x1
                if y1 + diameter > h:
                    diameter = h - y1
                shield_size = diameter, diameter
                ang_vel = 2.0
                degree = degree + ang_vel

                if degree > 360:
                    degree = 0
                height, width, col = firstPicture.shape
                centering = (width // 2, height // 2)
                M1 = cv2.getRotationMatrix2D(centering, round(degree), 1.0)
                M2 = cv2.getRotationMatrix2D(centering, round(360 - degree), 1.0)
                rotated1 = cv2.warpAffine(firstPicture, M1, (width, height))
                rotated2 = cv2.warpAffine(secondPicture, M2, (width, height))

                if diameter != 0:
                    img = transparent(rotated1, x1, y1, shield_size)
                    img = transparent(rotated2, x1, y1, shield_size)
                    # Start the animation from the beginning
                    count = 0
                    areThereHandsInWebcamVid = True
                    animation(count)

    else:
        # Switch back to displaying catInHat.png
        gif_label.configure(image=oriPhoto)
        areThereHandsInWebcamVid = False

    image = convert_image(img)
    draw_image(image)
    gameRoot.update()

    if cv2.waitKey(1) == ord('q') or not tk.Toplevel.winfo_exists(gameRoot):
        break

webcamRecording.release()
cv2.destroyAllWindows()