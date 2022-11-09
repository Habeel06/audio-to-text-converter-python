import speech_recognition as sr
import pyttsx3

print(r"By default the files will be saved at:C:\Users\HP")
a=str(input("Name of the file:"))


  
while ".mp3" in a:
        print("It will not work, use only text based files.I have saved it for another project or I will just fix this .")
    
        a=str(input("Name of the file:"))

r=sr.Recognizer()

#audio into text
def SpeakText(command):

    engine=pyttsx3.init()
    engine.say(command)

    # engine.save_to_file('MyText','voicerecognizer.mp3')
    engine.runAndWait()

with sr.Microphone() as source:
    print("listening....")
    r.adjust_for_ambient_noise(source, duration=0.2) #adjusting
    audio= r.listen(source)#listening
  

    MyText=r.recognize_google(audio)#recognizing voice
    MyText=MyText.lower()

    print(MyText)


print(a)
file = open(a, 'w')
file.write(MyText)
file.close()
print("File written successfully! ")



