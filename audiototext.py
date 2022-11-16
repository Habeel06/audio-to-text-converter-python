import speech_recognition as sr
import pyttsx3
from termcolor import colored
import colorama 
colorama.init()
import os
os.system('color')
print(colored('''
\n
\n
 __     __           __                            _______                                                     __                               
/  |   /  |         /  |                          /       \                                                   /  |                              
$$ |   $$ | ______  $$/   _______   ______        $$$$$$$  |  ______    _______   ______    ______   _______  $$/  ________   ______    ______  
$$ |   $$ |/      \ /  | /       | /      \       $$ |__$$ | /      \  /       | /      \  /      \ /       \ /  |/        | /      \  /      \ 
$$  \ /$$//$$$$$$  |$$ |/$$$$$$$/ /$$$$$$  |      $$    $$< /$$$$$$  |/$$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$$  |$$ |$$$$$$$$/ /$$$$$$  |/$$$$$$  |
 $$  /$$/ $$ |  $$ |$$ |$$ |      $$    $$ |      $$$$$$$  |$$    $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  /  $$/  $$    $$ |$$ |  $$/ 
  $$ $$/  $$ \__$$ |$$ |$$ \_____ $$$$$$$$/       $$ |  $$ |$$$$$$$$/ $$ \_____ $$ \__$$ |$$ \__$$ |$$ |  $$ |$$ | /$$$$/__ $$$$$$$$/ $$ |      
   $$$/   $$    $$/ $$ |$$       |$$       |      $$ |  $$ |$$       |$$       |$$    $$/ $$    $$ |$$ |  $$ |$$ |/$$      |$$       |$$ |      
    $/     $$$$$$/  $$/  $$$$$$$/  $$$$$$$/       $$/   $$/  $$$$$$$/  $$$$$$$/  $$$$$$/   $$$$$$$ |$$/   $$/ $$/ $$$$$$$$/  $$$$$$$/ $$/       
                                                                                          /  \__$$ |                                            
                                                                                          $$    $$/                                             
                                                                                           $$$$$$/                                            ''','cyan'))

print(colored("Report a bug at: https://github.com/Habeel06/audio-to-text-converter-python",'red'))
print(colored("By default the files will be saved at the location of this file.",'yellow'))
while True:
   a=str(input(colored("Name of the file(including extension-txt,vbs,html etc):","green")))
  while ".mp3" in a:
        print("It will not work, use only text based files.I have saved it for another project or I will just fix this .")
    
        a=str(input("Name of the file(including extension-txt,vbs,html etc):"))

    r=sr.Recognizer()

    #audio into text
    def SpeakText(command):

        engine=pyttsx3.init()
        engine.say(command)

    
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
    print(colored("File written successfully! ",'blue'))



