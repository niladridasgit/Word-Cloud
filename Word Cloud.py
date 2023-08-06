# Word Cloud
import os
import numpy as np
import cv2
import random as rd
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def design(s,end="\n"):
    print("--------------------------------------------------")
    print(s,end=end)
    print("--------------------------------------------------")

# creating myWordCloud class
class myWordCloud:
    # variables
    _directory = None
    _textFileName = None
    _wordCloudFileName = None

    # storing all the words from the text file into this list
    wordList = []

    # punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~=0123456789'''
    punctuationList = [i for i in punctuations]

    # uninterersting words
    uninterestingWords = ["on","so","in", "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i",\
         "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",\
              "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were",\
                   "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from",\
                        "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no",\
                             "nor", "too", "very", "can", "will", "just"]

    # constructor
    def __init__(self,directory,textFileName,wordCloudFileName):
        self._directory=directory
        # go to the directory
        os.chdir(self._directory)
        self._textFileName=textFileName
        self._wordCloudFileName=wordCloudFileName
    
    # access the text file and store all the words from the text file into wordList
    def accessTextFile(self):
        textOnFile=open(self._textFileName,"r")
        text=textOnFile.read()
        text=text.lower()
        # eliminate all the puncuations from the text
        for p in self.punctuationList:
            text=text.replace(p,' ')
        self.wordList=text.split()
    
    # clearing wordList
    def clearWordList(self):
        # eliminate all the white spaces from each word in wordList
        for i in range(0,len(self.wordList),1):
            self.wordList[i]=self.wordList[i].replace(" ","")
        
        # eliminate all the uninterested words from wordList
        for i in self.wordList:
            if i in self.uninterestingWords:
                self.wordList.remove(i)
        
        # eliminate all the same words from wordList
        flagList=[]
        flag=0
        for i in range(0,len(self.wordList),1):
            for j in range(i+1,len(self.wordList),1):
                if self.wordList[i]==self.wordList[j]:
                    flag=1
                    break
                else:
                    flag=0
            if flag==1:
                flagList.append(self.wordList[i])
        for i in flagList:
            self.wordList.remove(i)

        return " ".join(self.wordList)+" " 

    # creating automatic word cloud image using WordCloud module
    def automaticWordCloud(self,myString):
        wc = WordCloud(background_color = 'white',max_font_size=50,width=500,height=100).generate(myString)
        
        print("THE NUMBER OF WORDS IN THE STRING : "+str(len(self.wordList)))
        print("--------------------------------------------") 
        print("THE WORDS ARE : ",self.wordList)

        # save and display the generated image
        plt.imshow(wc)
        plt.axis("off")
        plt.savefig(self._wordCloudFileName)
        plt.show()

    # creating manual word cloud image with the words from wordList
    def manualWordCloud(self):
        print("THE NUMBER OF WORDS IN THE STRING : "+str(len(self.wordList)))        
        print("--------------------------------------------") 
        print("THE WORDS ARE : ",self.wordList)
        
        # CREATING AN IMAGE OBJECT :
        if len(self.wordList)<=10:
            xAxis=750 
        elif len(self.wordList)>=11 and len(self.wordList)<=50:
            xAxis=1500
        elif len(self.wordList)>=51 and len(self.wordList)<=100:
            xAxis=3000
        elif len(self.wordList)>=101 and len(self.wordList)<=200:
            xAxis=6000 
        else:
            xAxis=9000
        img=np.ones([500, xAxis, 3],dtype = np.uint8)

        # CHANGING THE BACKGROUND COLOR OF THE IMAGE : 
        img[:,:,:]=[100,200,255]
        
        # SETTING TEXT LOCATIONS : 
        flag=0
        Folow=0
        Left=100
        for i in range(0,len(self.wordList),1):
            if flag == 1:
                break
            # TEXT LOCATION : 
            # FROM LEFT : 
            Left=Left+100
            Top=200
            Last=(i+(2*i))+1
            for j in range(Folow,Last,1):
                if j == len(self.wordList):
                    flag = 1
                    break
                # FROM TOP : 
                if j<(Last-i):
                    Top-=50
                elif j==(Last-i):
                    Top=200
                else:
                    Top+=50
                textLocation=(Left,Top)
                # FONT STYLE : 
                fontStyle=rd.randrange(0,8,1)
                # FONT SIZE : 
                fontSize=rd.randrange(1,3,1)/(2)
                # FONT COLOR : 
                R=40*(fontSize+1)
                G=50*(fontSize+0.5)
                B=60*(fontSize)
                fontColor=(int(B),int(G),int(R))
                # FONT WIDTH : 
                fontWidth=int(fontSize+1)
                # PUTTING TEXT ON THE IMAGE : 
                cv2.putText(
                    img,
                    self.wordList[j],
                    textLocation,
                    fontStyle,
                    fontSize,
                    fontColor,
                    fontWidth)
                # WRITING/SAVING THE IMAGE : 
                cv2.imwrite(self._wordCloudFileName,img)
            Folow=Last
        # SHOWING THE IMAGE : 
        cv2.imshow(self._wordCloudFileName,img)
        cv2.waitKey(0)

design(r'[SUGGESTION] THE PATH OF OUR WORKING FILE DIRECTORY : C:\Users\junil\Desktop\Python\Projects\Project 3 - Word Cloud Application')
o=input("DO YOU WANT TO CHANGE THE PATH : YES/NO : ")
if o.upper()=="YES":
    directory = input("[ENTER] THE PATH OF OUR WORKING FILE DIRECTORY : ")
else:
    directory=r"C:\Users\junil\Desktop\Python\Projects\Project 3 - Word Cloud Application"

design(r'[SUGGESTION] THE NAME OF OUR INPUT TEXT FILE : input.txt')
o=input("DO YOU WANT TO CHANGE THE NAME : YES/NO : ")
if o.upper()=="YES":
    iname = input("[ENTER] THE NAME OF OUR INPUT TEXT FILE : [SUGGESTION] WITH EXTENSION : ")
else:
    iname=r"input.txt"

design(r'[SUGGESTION] THE NAME OF OUR OUTPUT TEXT FILE : output.png')
o=input("DO YOU WANT TO CHANGE THE NAME : YES/NO : ")
if o.upper()=="YES":
    oname = input("[ENTER] THE NAME OF OUR OUTPUT TEXT FILE : [SUGGESTION] WITH EXTENSION : ")
else:
    oname=r"output.png"

os.chdir(directory)
if os.path.exists(oname):
    os.remove(oname)

# create a WordCloud object/instance
myCloud=myWordCloud(directory,iname,oname)

# menu
print("""
    --------------------------
    [OPTION] CHOOSE AN OPTION : 
    1. AUTOMATIC WORDCLOUD
    2. MANUAL WORDCLOUD
    --------------------------
    """)
c=int(input())
# automatic
if c==1:
    myCloud.accessTextFile()
    myCloud.automaticWordCloud(myCloud.clearWordList())
# manual
elif c==2:
    myCloud.accessTextFile()
    myCloud.clearWordList()
    myCloud.manualWordCloud()
else:
    print("WRONG OPTION!")