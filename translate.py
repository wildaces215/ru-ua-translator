from gettext import install
from argostranslate import package, translate
import sys

class Translator():
    def __init__(self):
        super().__init__()

    def checkText(self,ruText):
        if ruText == None:
            return "No Text is inputed"
    
    def translateRussianText(self,ruText):
        langs = translate.get_installed_languages()
        translated_eng = ''
        for i in langs:
            if str(i) == 'Russian':
                translator = langs[1].get_translation(langs[0])
                translated_eng =translator.translate(ruText)
                break
            
        return translated_eng
    
    

ru_text= sys.argv[1]



app = Translator()

app.checkText(ru_text)
print(app.translateRussianText(ru_text))

