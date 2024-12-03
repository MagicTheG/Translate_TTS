from gtts import gTTS
import googletrans
from googletrans import Translator
from playsound import playsound

translator = Translator()

def translate():
    LanguageTranslate = input("Enter the lanauage you want to translate to based on the language code (ex. es(Spanish), ar(Arabic) etc..) " )
    Input = input("Please Enter The Phrase You Want to Translate: " )

    translated = translator.translate(Input, dest= LanguageTranslate)
    print(f"Translated Text: {translated.text}")

    tts = gTTS(translated.text, lang = LanguageTranslate)
    tts.save("TranslatedOutput.mp3")
    print ("Now Playing Audio")
    playsound("TranslatedOutput.mp3")
    
def main():
    
    LangCode = input("Welcome! If you know your language code, please type 1 to translate. If not, type 0 to see the languages or -1 to exit. ")
    IntLangCode = int(LangCode)
    if IntLangCode == 1 :
        translate()
    elif IntLangCode == 0:
        for lang, code in googletrans.LANGCODES.items():
                print(f"{lang.title()} ({code})")
                print("\n")
        translate()
    elif IntLangCode == -1:
        print("Thank you for using the translator. See you Next Time! ")
    else: 
        print("Invlid Input, Try again.")

if __name__ == "__main__":
    main()




