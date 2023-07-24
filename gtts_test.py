
from gtts import gTTS


#Write your text
text_to_speech = "Bonjour j'utilise python !"

#Choose your language (en : english, fr: french, ...)
language = "fr"

#Passing the text, language and the speed to the module
myobj = gTTS(text=text_to_speech, lang=language, slow=False)

#Saving the audio in mp3
myobj.save("text_to_speech.mp3")

file = "text_to_speech.mp3"

