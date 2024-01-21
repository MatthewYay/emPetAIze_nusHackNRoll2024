# These codes were solely written by MATTHEW NG WEI CHEN during the Hack&Roll 2024 hackathon, which was graciously organised by NUS Hackers!
# I deeply thank their team for giving me this wonderful opportunity to showcase my passion project. The event really means a lot to me.
# Also, if you are referencing my work, please credit me:
# GitHub : @MatthewYay
# LinkedIn : https://www.linkedin.com/in/matthew-ng-wc/

from textblob import TextBlob

def word_polarity(test_subset):
    listOfPositiveWords=[]
    listOfNegativeWords=[]
    listOfNeutralWords=[]
    for word in test_subset:
        testimonial = TextBlob(word)
        if testimonial.sentiment.polarity >= 0.5:
            listOfPositiveWords.append(word)
        elif testimonial.sentiment.polarity <= -0.5:
            listOfNegativeWords.append(word)
        else:
            listOfNeutralWords.append(word)
    print("Positive words:",listOfPositiveWords)
    print("Negative words:",listOfNegativeWords)
    print("Neutral words:",listOfNeutralWords)


sentence = input("Type something:  ")
word_list = sentence.split()
word_polarity(word_list)

#print("Testi!ng some Stuff & 2 IIO **&$wkfhed 013#} wsocjnW".lower())


