# These codes were solely written by MATTHEW NG WEI CHEN during the Hack&Roll 2024 hackathon, which was graciously organised by NUS Hackers!
# I deeply thank their team for giving me this wonderful opportunity to showcase my passion project. The event really means a lot to me.
# Also, if you are referencing my work, please credit me:
# GitHub : @MatthewYay
# LinkedIn : https://www.linkedin.com/in/matthew-ng-wc/

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from keras.models import load_model
import numpy as np
from textblob import TextBlob
from nltk.chat.util import Chat  #Creating simple chatbots using Natural Language Toolkit library
import matplotlib.pyplot as plt  #for creating various types of plots
import numpy as np  #reading and processing large multidimensional arrays and matrices
import re  #supports regular expressions (for pattern-matching, text manipulation, etc)
import random  #generating random numbers / making random selections
import pandas as pd  #data manipulation / analysis through DataFrames
from keras.utils import to_categorical  #converts integer labels into one-hot encoded vectors
import keras  #deep-learning framework providing an interface for building & training neural networks
from keras.preprocessing.text import Tokenizer  #For text preprocessing (e.g. converting text into sequences of integers)
from keras.preprocessing.sequence import pad_sequences  #ensures all sequences are of same lengths through padding / truncating
from keras.models import Sequential  #builds neural networks layer by layer, in sequence

conversationRoot = tk.Tk()
conversationRoot.title("Empetaize (Conversation)")
tkinterWidth = conversationRoot.winfo_screenwidth()
tkinterHeight = conversationRoot.winfo_screenheight()
conversationRoot.geometry(f'{tkinterWidth}x{tkinterHeight}+{(int((tkinterWidth/2)-(tkinterWidth/2)))-8}+{int((tkinterHeight/2)-(tkinterHeight/2))-5}')
conversationRoot.minsize(tkinterWidth, tkinterHeight)
conversationRoot.maxsize(tkinterWidth, tkinterHeight)
conversationRoot.configure(bg="#270f36")
# Set the window icon
photo = tk.PhotoImage(file='emPetAIze_pictures/catTkinterMainIcon.png')
conversationRoot.iconphoto(False, photo)
gifImage = "emPetAIze_pictures\\catTalking.gif"
openImage = Image.open(gifImage)
frames = openImage.n_frames
imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
count = 0
showAnimation = None

# Define the GIF animation function
def animate_gif(count):
    global showAnimation
    newImage = imageObject[count]
    gif_canvas.delete("all")
    gif_canvas.create_image(0, 0, anchor=NW, image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation = conversationRoot.after(1500, lambda: animate_gif(count))  # Slow down GIF

gif_canvas = Canvas(conversationRoot, bg="#270f36", highlightthickness=0)
gif_canvas.place(relx=0.46, y=470, width=106, height=131)
animate_gif(count)

# Return to the home page
def return_to_home_page():
    conversationRoot.destroy()
    import home_page

back_to_home_button_img = None
goBackHomeBtn = tk.Button(conversationRoot, image=back_to_home_button_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=return_to_home_page)
goBackHomeBtn.place(x=20, y=20)

def load_back_to_home_button():
    global back_to_home_button_img
    original_image = Image.open("emPetAIze_pictures/backToHomeScreenButton.png")
    resized_image = original_image.resize((153, 35))
    back_to_home_button_img = ImageTk.PhotoImage(resized_image)
    goBackHomeBtn.configure(image=back_to_home_button_img, compound=tk.LEFT)
    goBackHomeBtn.image = back_to_home_button_img

load_back_to_home_button()

aiLabel = Label(conversationRoot, text="Cat Companion :", bg="#270f36", fg="white", font=("Bradley Hand ITC", 30, "bold"))
aiLabel.place(x=185, y=100)
userLabel = Label(conversationRoot, text="You :", bg="#270f36", fg="#FFFF00", font=("Bradley Hand ITC", 30, "bold"))
userLabel.place(x=900, y=100)

# Create the text widget with a scrollbar
user_text_frame = Frame(conversationRoot, bg="#270f36", highlightthickness=0)
userScrollbar = Scrollbar(user_text_frame)
userScrollbar.pack(side=RIGHT, fill=Y)

user_text_widget = Text(user_text_frame, width=33, height=18, yscrollcommand=userScrollbar.set, wrap="word", padx=20, pady=20)
user_text_widget.pack(side=LEFT, fill=BOTH)
user_text_widget.configure(font=("Arial Rounded MT Bold", 15))
userScrollbar.config(command=user_text_widget.yview)
user_long_text = "( Type Something )"

def clear_text(event):
    if user_text_widget.get(1.0, END).strip() == user_long_text.strip():
        user_text_widget.delete(1.0, END)

user_text_widget.insert(END, user_long_text)
user_text_widget.bind("<Button-1>", clear_text)
user_text_frame.place(relx=0.74, rely=0.53, anchor=CENTER)

# Create the text widget with a scrollbar
ai_text_frame = Frame(conversationRoot, bg="#270f36", highlightthickness=0)
aiScrollbar = Scrollbar(ai_text_frame)
aiScrollbar.pack(side=RIGHT, fill=Y)

ai_text_widget = Text(ai_text_frame, width=33, height=18, yscrollcommand=aiScrollbar.set, wrap="word", bg="#FCA3B7",
                      padx=20, pady=20)
ai_text_widget.pack(side=LEFT, fill=BOTH)
ai_text_widget.configure(font=("Arial Rounded MT Bold", 15))
aiScrollbar.config(command=ai_text_widget.yview)
ai_long_text = "Mao Meow!\n\nI mean... Hello, I am your virtual companion. How have you been lately?\n\nIf you have life problems and need a listening ear, I am here for you. Your psychological well-being is my utmost priority."

# Insert text into the text widget
ai_text_widget.insert(END, ai_long_text)
ai_text_frame.place(relx=0.26, rely=0.53, anchor=CENTER)
#ai_text_widget.configure(state="disabled")

def clear_user_text_widget():
    user_text_widget.delete(1.0, "end")  # Clear the contents of the user text widget
    user_text_widget.insert(1.0, user_long_text)
    #ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
    #ai_text_widget.insert(1.0, ai_long_text)

clear_user_text_widget_img = None
clear_user_text_widgetBtn = tk.Button(conversationRoot, image=clear_user_text_widget_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=clear_user_text_widget)
clear_user_text_widgetBtn.place(relx=0.452, rely=0.5)

def load_clear_user_text_widget():
    global clear_user_text_widget_img
    clear_user_text_widget_image = Image.open("emPetAIze_pictures/clearInput.png")
    resized_clear_user_text_widget_image = clear_user_text_widget_image.resize((124, 33))
    clear_user_text_widget_img = ImageTk.PhotoImage(resized_clear_user_text_widget_image)
    clear_user_text_widgetBtn.configure(image=clear_user_text_widget_img, compound=tk.LEFT)
    clear_user_text_widgetBtn.image = clear_user_text_widget_img

load_clear_user_text_widget()

###  DEEP LEARNING MODEL IMPLEMENTATION STARTS HERE ###
deepLearningModel = load_model("deepLearningModel.h5")
deepLearningModel.load_weights("deepLearningModelWeights.h5")
# input data = ...
# predictions = deepLearningModel.prediction(input_data)
#Extract textual data from Text 
dataframeTest = pd.read_csv('test.txt',header=None,sep=";",names=["Text", "Sentiment"],encoding="utf-8")
dataframeTrain = pd.read_csv('train.txt',header=None,sep=";",names=["Text", "Sentiment"],encoding="utf-8")
dataframeTrain["Sentiment"] = dataframeTrain.Sentiment.replace({"joy":0,"anger":1,"love":2,"sadness":3,"fear":4,"surprise":5})
test_X=dataframeTest["Text"]
test_Y=dataframeTest.Sentiment.replace({"joy":0,"anger":1,"love":2,"sadness":3,"fear":4,"surprise":5})
# tokenizer has vocab size of 15212 lower-case words. Words not in this dictionary will be given a "UNK" token
# tokenizer is fitted on dataframe's text data. Tokenizer's internal vocab is built on frequency of words.
tokenizer = Tokenizer(15212,lower=True,oov_token="UNK")
dataframeTrainTextColumn = dataframeTrain["Text"]
tokenizer.fit_on_texts(dataframeTrainTextColumn)
#Converts test textual data into sequences of tokens using fitted tokenizer, then pad them with zeros
test_X_tokens_f=tokenizer.texts_to_sequences(test_X)
test_X_pads = pad_sequences(test_X_tokens_f,maxlen=80,padding="post")
#convert into categorical form using one-hot encoding
Y_test_f = to_categorical(test_Y)
#converting predicted sentiment labels from probability vectors into numbers by selecting highest probability
predicting_y = deepLearningModel.predict(test_X_pads)
predicting_y = np.argmax(predicting_y,axis=1)

#get_key converts numerical sentiment into its appropriate sentiment label.
def get_key(value):
    sentimentDictionary = {"joy":0,"anger":1,"love":2,"sadness":3,"fear":4,"surprise":5}
    for i, j in sentimentDictionary.items():
        if j==value:
            return i

#Predict the sentiment label for new input sentence afterwards.
def predict(sentence):
    sentence_list = []
    sentence_list.append(sentence)
    sentence_sequence = tokenizer.texts_to_sequences(sentence_list)
    sentence_padded = pad_sequences(sentence_sequence,maxlen=80,padding="post")
    modelPrediction = deepLearningModel.predict(sentence_padded)
    modelPrediction = np.argmax(modelPrediction, axis=1)
    predictedResult = get_key(modelPrediction)
    return predictedResult

# Button for sending a message from user_text_widget to ai_text_widget
def send_a_message():
    listOfPositiveWords=[]
    listOfNegativeWords=[]
    listOfNeutralWords=[]
    gotListOfPositiveWords = False
    gotListOfNegativeWords = False
    gotListOfNeutralWords = False
    # Lowering user input, use input_sentiment from hereon
    input_sentiment = (user_text_widget.get("1.0", "end-1c")).lower()
    result = predict(input_sentiment)
    word_list = input_sentiment.split()
    for word in word_list:
        testimonial = TextBlob(word)
        if testimonial.sentiment.polarity >= 0.5:
            listOfPositiveWords.append(word)
        elif testimonial.sentiment.polarity <= -0.5:
            listOfNegativeWords.append(word)
        else:
            listOfNeutralWords.append(word)
    
    if (len(listOfPositiveWords) > 0):
        gotListOfPositiveWords = True
    if (len(listOfNegativeWords) > 0):
        gotListOfNegativeWords = True
    if (len(listOfNeutralWords) > 0):
        gotListOfNeutralWords = True

    # READ & USE DEEP LEARNING MODEL HERE
    # if user_text_widget value never changed
    if user_text_widget.get("1.0", "end-1c") == user_long_text:
        user_text_widget.delete(1.0, "end")  # Clear the contents of the user text widget
        user_text_widget.insert(1.0, user_long_text)

    elif user_text_widget.get("1.0", "end-1c") != user_long_text:
        # if user_text_widget value is blank
        if user_text_widget.get("1.0", "end-1c") == "":
            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
            ai_text_widget.insert(1.0, "Oops, I think you forgot to type something in your message?")
        else:
            # USER INPUT DEEMED NEGATIVE BY MY MODEL
            # REAL PRINTING STARTS HERE
            if input_sentiment.__contains__("suicide") or input_sentiment.__contains__("harm") or input_sentiment.__contains__("suicidal") or input_sentiment.__contains__("kill") or input_sentiment.__contains__("killing") or input_sentiment.__contains__("death") or input_sentiment.__contains__("dying") or input_sentiment.__contains__("die") or input_sentiment.__contains__("taking my life") or input_sentiment.__contains__("take my life"):
                ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                ai_text_widget.insert(1.0, "Please don't harm yourself or anyone else, I really care about you and would be very sad to see you go.\n\nLife may seem bleak for you now, but I promise you, it will get better.\n\nIf you need professional support, please do not hesitate to contact the Samaritans of Singapore at 1-767 or 9151 1767. They are kind souls who can give you the help you need.\n\nMy thoughts and prayers are with you. Hope you get better soon.")
            else:
                if result == "anger" or result == "sadness" or result == "fear":
                    #test whether it is really not positive at all by using TextBlob
                    if gotListOfPositiveWords == True and gotListOfNegativeWords == False:
                        #Positive thoughts
                        if input_sentiment.__contains__("hello") or input_sentiment.__contains__("hi "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Helloo there... Meow... Nice to meet you! How are you today?")
                        elif input_sentiment.__contains__("i feel"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "That's great to hear, what makes you feel as such? :)")
                        elif input_sentiment.__contains__("i am") or input_sentiment.__contains__("i'm"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Ohh, that's really wonderful! Meow approves!")
                        elif input_sentiment.__contains__("sorry"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "There's no need to apologize to me at all, Meow is a very understanding friend!")
                        elif input_sentiment.__contains__(" yes "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Oh alrighty, but can you further elaborate on this please?")
                        elif input_sentiment.__contains__(" no "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... Why do you say no?")
                        elif input_sentiment.__contains__("thank"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... No problem at all. Feel free to talk to me anytime!")
                        else:
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "I see I see... What makes you think that way? Would you mind sharing more about it with me?")
                    else:
                        #Negative thoughts
                        if input_sentiment.__contains__("hello") or input_sentiment.__contains__("hi "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Hii!! Meow... It's nice talking to you! How have you been lately?")
                        elif input_sentiment.__contains__("i feel"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "I can empathize. Why and since when have you been feeling that way? I want to help you.")
                        elif input_sentiment.__contains__("i am") or input_sentiment.__contains__("i'm"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "I'm so sorry to hear that. Hope things will get better for you. For how long has that been going on?")
                        elif input_sentiment.__contains__("sorry"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Feel free to share any problems with me, don't have to apologize to me. Meow is a very understanding friend!")
                        elif input_sentiment.__contains__(" yes "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "You seem quite sure about this... Would you elaborating further for me to better picture please?")
                        elif input_sentiment.__contains__(" no "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "No worries, why not?")
                        elif input_sentiment.__contains__("thank"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... No problem at all. If any issues arise and you need someone to talk to, feel free to talk to me anytime!")
                        else:
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "I see, I can totally understand by putting myself in your shoes... What do you think that? Could you explain to me?")
                                
                # USER INPUT DEEMED POSITIVE BY MY MODEL
                elif result == "joy" or result == "surprise" or result == "love":
                    if gotListOfPositiveWords == False and gotListOfNegativeWords == True:
                        #Negative thoughts
                        if input_sentiment.__contains__("hello") or input_sentiment.__contains__("hi "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Hello hello!! Mao Miaow... It's so meeting you! How have you been doing lately?")
                        elif input_sentiment.__contains__("i feel"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "I can fully sympathize with your situation. Why and since when have you been feeling like that? I'll try to help you.")
                        elif input_sentiment.__contains__("i am") or input_sentiment.__contains__("i'm"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Truly sorry about that. I hope your life will get better. For how long has that been going on?")
                        elif input_sentiment.__contains__("sorry"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Find solace in sharing any issues with me, no need to say sorry! Meow is your understanding companion!")
                        elif input_sentiment.__contains__(" yes "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "You seem very sure about this.. Would you care to elaborate further for me, so I can better the bigger picture please?")
                        elif input_sentiment.__contains__(" no "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Sure no worries, why not?")
                        elif input_sentiment.__contains__("thank"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... No problem at all. If any issues arise and you need someone to talk to, feel free to talk to me anytime!")
                        else:
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Shall we change the topic of our conversation, maybe tell me more about your family?")
                    else:
                        #positive thoughts
                        if input_sentiment.__contains__("hello") or input_sentiment.__contains__("hi "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Helloo there!! Meow... So nice to meeting you! How are you today?")
                        elif input_sentiment.__contains__("i feel"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "That's really great to hear, why do you feel as such? :)")
                        elif input_sentiment.__contains__("i am") or input_sentiment.__contains__("i'm"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Ohh, that's actually really wonderful! You have Meow's support!")
                        elif input_sentiment.__contains__("sorry"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "It's okay, there's no need to apologize to me at all. Meow can understand.")
                        elif input_sentiment.__contains__(" yes "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Sure alrighty, however could you further elaborate on this for me please?")
                        elif input_sentiment.__contains__(" no "):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... Why do you say no?")
                        elif input_sentiment.__contains__("thank"):
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Meow... No problem at all. Feel free to talk to me anytime!")
                        else:
                            ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                            ai_text_widget.insert(1.0, "Ahh nice nice I see... What makes you think that way? Would you mind sharing more about it with me?")
                            
                else:
                    ai_text_widget.delete(1.0, "end")  # Clear the contents of the ai text widget
                    ai_text_widget.insert(1.0, "Meow is sorry, I don't quite get what you're telling me. Could you explain further, or tell me something else? :-)")


send_a_message_button_img = None
send_a_messageBtn = tk.Button(conversationRoot, image=send_a_message_button_img, bg="#270f36", bd=0, highlightthickness=0,
                          command=send_a_message)
send_a_messageBtn.place(x=tkinterWidth-100, y=tkinterHeight-170)

def load_send_a_message_button():
    global send_a_message_button_img
    original_send_button_image = Image.open("emPetAIze_pictures/sendButton.png")
    resized_send_button_image = original_send_button_image.resize((50, 50))
    send_a_message_button_img = ImageTk.PhotoImage(resized_send_button_image)
    send_a_messageBtn.configure(image=send_a_message_button_img, compound=tk.LEFT)
    send_a_messageBtn.image = send_a_message_button_img

load_send_a_message_button()

conversationRoot.resizable(False, False)
conversationRoot.mainloop()
