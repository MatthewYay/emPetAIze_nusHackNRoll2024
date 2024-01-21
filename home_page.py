# These codes were solely written by MATTHEW NG WEI CHEN during the Hack&Roll 2024 hackathon, which was graciously organised by NUS Hackers!
# I deeply thank their team for giving me this wonderful opportunity to showcase my passion project. The event really means a lot to me.
# Also, if you are referencing my work, please credit me:
# GitHub : @MatthewYay
# LinkedIn : https://www.linkedin.com/in/matthew-ng-wc/

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def animate_gif():
    global count
    if homeRoot.winfo_exists(): # Check if the window still exists
        transparentHomeCanvas.itemconfig(gif_item, image=resize_img[count])
        count += 1
        if count > last_frame:
            count = 0
        anim = homeRoot.after(400, animate_gif)

def resizeImage(image, newWidth, newHeight):
    return image.resize((newWidth, newHeight), Image.LANCZOS)

homeRoot = tk.Tk()
homeRoot.title("Empetaize (Home)")
photo = tk.PhotoImage(file='emPetAIze_pictures/catTkinterMainIcon.png')
homeRoot.iconphoto(False, photo)
tkinterWidth = homeRoot.winfo_screenwidth()
tkinterHeight = homeRoot.winfo_screenheight()
homeRoot.geometry(f'{tkinterWidth}x{tkinterHeight}+{(int((tkinterWidth/2)-(tkinterWidth/2)))-8}+{int((tkinterHeight/2)-(tkinterHeight/2))-5}')
homeRoot.minsize(tkinterWidth, tkinterHeight)
homeRoot.maxsize(tkinterWidth, tkinterHeight)
homeRoot.configure(bg="#270f36")
transparentHomeCanvas = tk.Canvas(homeRoot, bg="#270f36", width=tkinterWidth-0, height=round((tkinterWidth-20)/500*200), bd=0, highlightthickness=0)
transparentHomeCanvas.place(x=10, y=20)
transparentHomeCanvas.delete("all")
gif_image = Image.open('emPetAIze_pictures/auroraBorealis.gif')
last_frame = gif_image.n_frames - 1
gif_frames = []
resize_img = []

for frame_index in range(gif_image.n_frames):
    gif_image.seek(frame_index)
    frame = gif_image.copy()
    gif_frames.append(frame)
    # Increase the size of the resized GIF by multiplying the width and height
    gif_frame_resized = resizeImage(frame, tkinterWidth-20, round((tkinterWidth-20)/500*200))
    resize_img.append(ImageTk.PhotoImage(gif_frame_resized))

# Place the GIF image at the top layer
count = 0
gif_item = transparentHomeCanvas.create_image(0, 0, anchor="nw", image=resize_img[0])

# Adding catHuggingGirl.png
cat_hugging_girl_img = Image.open("emPetAIze_pictures/catHuggingGirl.png")
resized_cat_hugging_girl = cat_hugging_girl_img.resize((391, 521))
cat_hugging_girl_tk_img = ImageTk.PhotoImage(resized_cat_hugging_girl)
cat_hugging_girl_item = transparentHomeCanvas.create_image(0, 505, anchor=tk.SW, image=cat_hugging_girl_tk_img)

# Adding empetaize_logo.png
empetaize_logo_img = Image.open("emPetAIze_pictures/empetaize_logo.png")
resized_empetaize_logo = empetaize_logo_img.resize((459, 177))
empetaize_logo_tk_img = ImageTk.PhotoImage(resized_empetaize_logo)
empetaize_logo_item = transparentHomeCanvas.create_image((tkinterWidth-400)/2, 10, anchor=tk.NW, image=empetaize_logo_tk_img)

#transparentHomeCanvas.lift(gif_item)  # Lift the GIF item to the top layer
animate_gif()

# Place the "testingSomethingg.png" image at the bottom right corner
testing_something_img = Image.open("emPetAIze_pictures/wordsOfEncouragement.png")
resized_testing_something = testing_something_img.resize((780, 312))
testing_something_tk_img = ImageTk.PhotoImage(resized_testing_something)
testing_something_item = transparentHomeCanvas.create_image(1220, 490, anchor="se", image=testing_something_tk_img)

def go_to_ConversationPage():
    homeRoot.destroy() # Hide the current window
    import conversation_page # Import the game_page module
    conversation_page.conversationRoot # Show the game_page.py window

talk_with_meow_img = None
goTalkWithMeowBtn = tk.Button(homeRoot, image=talk_with_meow_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=go_to_ConversationPage)
goTalkWithMeowBtn.place(x=tkinterWidth/10*2.35, y=tkinterHeight/18*14)
leftTalkButtonImg = Image.open("emPetAIze_pictures/talkWithMeowButton.png")
resized_imageLeftBtn = leftTalkButtonImg.resize((206, 42))
talk_with_meow_img = ImageTk.PhotoImage(resized_imageLeftBtn)
goTalkWithMeowBtn.configure(image=talk_with_meow_img, compound=tk.CENTER)
goTalkWithMeowBtn.image = talk_with_meow_img

def go_to_GamePage():
    homeRoot.destroy() # Hide the current window
    import game_page # Import the game_page module
    game_page.gameRoot # Show the game_page.py window

play_with_meow_img = None
goPlayWithMeowBtn = tk.Button(homeRoot, image=play_with_meow_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=go_to_GamePage)
goPlayWithMeowBtn.place(x=tkinterWidth/10*6, y=tkinterHeight/18*14)
rightPlayButtonImg = Image.open("emPetAIze_pictures/playWithMeowButton.png")
resized_imageRightBtn = rightPlayButtonImg.resize((210, 42))
play_with_meow_img = ImageTk.PhotoImage(resized_imageRightBtn)
goPlayWithMeowBtn.configure(image=play_with_meow_img, compound=tk.CENTER)
goPlayWithMeowBtn.image = play_with_meow_img

homeRoot.resizable(False, False)
homeRoot.mainloop()
