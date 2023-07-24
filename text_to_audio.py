from playsound import playsound
from gtts import gTTS

def text_to_audio_func(face_names):
    #Write your text
    recognition_name = "Bonjour " + str(face_names) + " j'espère que tu vas bien !"

    #Choose your language (en : english, fr: french, ...)
    language = "fr"

    #Passing the text, language and the speed to the module
    myobj = gTTS(text=recognition_name, lang=language, slow=False)

    #Saving the audio in mp3
    myobj.save("recognition_name.mp3")
    file = "recognition_name.mp3"
    print("Bonjour" + str(face_names) + " j'espère que vous allez bien !")
    playsound("recognition_name.mp3")


