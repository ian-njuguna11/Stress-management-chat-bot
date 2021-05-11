# //Betty...
#Import libraries
# from logging import root
from IPython.utils.tests.test_wildcard import root
from newspaper import Article
import random
import string
# from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

from tkinter import *
import tkinter as tk



#ignore anny warnings
warnings.filterwarnings('ignore')

#Download pckgs from nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

#Get Artclie url
article = Article('https://www.brainline.org/article/stress-management-how-reduce-prevent-and-cope-stress')
article.download()
article.parse()
article.nlp()
corpus = article.text

#print corpus
# print(corpus)

# tockenization
text = corpus
sent_tokens = nltk.sent_tokenize(text)  # convert the text into a list of sentences

# print(sent_tokens)

#create a dictionary(key: value) pair to remove punctuations
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)
#punctuation
# print(string.punctuation)
#dictoinary
# print(remove_punct_dict)

def lemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

# print(lemNormalize(text))

# key word matching

# greeting input(wake word)
GREETING_INPUTS = ['hi', 'hello', 'holla', 'greetings', 'wassup', 'hey']

# GREETING RESPONSE
GREETING_RESPONSES = ['howdy', 'hi', 'hey', 'what\'s good', 'hello', 'hey there']


# function to return a random response to a user greeting
def greeting(sentence):
	# if the user's input is a greeting, then return a randomly chose greeting response
	for word in sentence.split():
		if word.lower() in GREETING_INPUTS:
			#  return random.choice(GREETING_RESPONSES)
			return random.choice(GREETING_RESPONSES)

def response(user_response):
  #the users response/query
  # user_response = 'What is coronavirus disease'

  user_response = user_response.lower()

  # print(user_response)

  robo_response = ' '

  #Append the users response to the sentense list
  sent_tokens.append(user_response)

  #print the sentence list after appending the users response
  # print(sent_tokens)

  #create a TfidVectorizer obj
  TfidVec =  TfidfVectorizer(tokenizer= lemNormalize, stop_words='english')

  #Convert the text to a matrix of TF-IDf features
  tfidf = TfidVec.fit_transform(sent_tokens)

  #print the TFIDF FEATURES
  # print(tfidf)

  #get the measure of the simmilarity
  # vals = cosine_similarity(tfidf[-1],tfdif)
  vals = cosine_similarity(tfidf[-1], tfidf)

  # print(vals)

  #get the index of thmost similar text/sentence to the users response
  idx = vals.argsort()[0][-2]

  # print(idx)

  #reduce the dimensionality of vals
  flat = vals.flatten()

  #sort the list in ascending order
  flat.sort()

  #get the most similar score to the users response
  score = flat[-2]

  #print th simmilarity score
  # print(score)

  #if val 'score' is 0 then there's no similar to the users response
  if(score == 0):
    robo_response=robo_response+'I apologize, I don\'t understand'
  else:
    robo_response=robo_response+sent_tokens[idx]

  #print the th bot response
  # print(robo_response)

  sent_tokens.remove(user_response)

  return robo_response

# flag = True
# print(' I will answer your queries about Stress management. If want to exit type bye')
# while(flag == True):
#   user_response =input()
#   user_response == user_response.lower()
#   if(user_response != "bye"):
#     if(user_response == "thanks" or user_response == "thank you"):
#       flag=False
#       print(" You are welcome")
#     else:
#       if(greeting(user_response) != None):
#         print(" "+greeting(user_response))
#       else:
#         print(" "+response(user_response))
#
#   else:
#     flag = False
#     print(" chat with you later !")


r = tk.Tk()


def send():
    send = "You => "+ e.get()
    txt.insert(END,"\n"+send)

    # print(' I will answer your queries about Stress management. If want to exit type bye')
    flag = True
    if (flag == True):
      user_response = send
      user_response == user_response.lower()
      if (user_response != "bye"):
          if (user_response == "thanks" or user_response == "thank you"):
            flag = False
            # print("You are welcome ")
            txt.insert(END, "\n" + "Counsellor => You are welcome")
          else:
            if (greeting(user_response) != None):
              # print(" " + greeting(user_response))
              txt.insert(END, "\n" + "Counsellor => "+ greeting(user_response))
            else:
              # print(" " + response(user_response))
              txt.insert(END, "\n" + "Counsellor => "+ response(user_response))
    else:
      flag = False
      # print(" chat with you later !")
      txt.insert(END, "\n" + "Counsellor => chat with you later !")
    e.delete(0,END)



txt = Text(r,bg = "green")
txt.insert(END,"\n"+ 'Counsellor => Hi, I will answer your queries about Stress management.\n If want to exit type bye')
txt.grid(row=0,column=0,columnspan=4)
e=Entry(r, width='100',bg = 'blue')
send=Button(r,text="Send",command=send,bg = "green").grid(row=1,column=1)
e.grid(row=1,column=2)
r.title('Counsellor Chatbot ')
r.mainloop()