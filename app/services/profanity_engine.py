from better_profanity import Profanity
from pathlib import Path

language_engines={}

def init_languages_engines():

    profanity_en = Profanity()
    profanity_en.load_censor_words()
    language_engines["english"] = profanity_en

    #Definimos la ruta de la carpeta
    folder_dics = Path("app/language_dicts")

    if not folder_dics.exists():
        raise FileExistsError("[INFO]La carpeta 'app/dicts' no existe. Imposible arrancar el motor de idiomas.")
    files=list(folder_dics.glob("*.txt"))
    if  len(files)== 0:
        raise ValueError("[INFO]La carpeta 'app/dicts' esta vacia. Faltan los diccionarios.")

    for file_path in folder_dics.glob("*.txt"):
        language_name = file_path.stem.lower()

        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f.readlines() if line.strip()]

        new_engine = Profanity()
        new_engine.load_censor_words(words)
        language_engines[language_name] = new_engine

# Ejecutamos la carga inicial dinamica
#init_language_engines()

#no entendi esto que pedo es un dict a pero que tiene el dict aaa nose instacias de Profanity
def proccesing_text(text: str, char: str, language: str) -> dict:

    selected_engine = language_engines.get(language.lower(), language_engines["english"])
    
    #aqui nomas consulamos si hay una mala palabra si si  a pues la invertimos
    appropriate = not selected_engine.contains_profanity(text)
    #aqui limpiamos, cesuramos con el char q se le fue pasado  y lo aguardamos
    clean_text = selected_engine.censor(text, char)

    profanity_count = 0 if appropriate else clean_text.count(char *4)
    #regresamos el texto en dic, podriamos incluso convertirlo en outputText no vedd tendriamos que importa el model y nose me han dicho que cada cosa haga lo suyo por tema de resposabilidad y seguridad
    return {
        "clean_text": clean_text,
        "appropriate": appropriate,
        "amount_censorship": profanity_count
    }

