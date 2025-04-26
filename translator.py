#pip install googletrans==4.0.0-rc1
#we have to install this module before running the program
from googletrans import Translator

translator =Translator()
txt=input()
output=translator.translate(txt,dest='en')
print(output.text)