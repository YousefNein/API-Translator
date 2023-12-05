import pandas as pd
from googletrans import Translator
import requests

def get_audio_and_example(word):
    headers = {"accept": "application/json"}
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url, headers=headers)
    json_data = response.json()

    audio_link = None
    example_sentence = None

    if json_data:
        entry = json_data[0] 
        phonetics = entry.get("phonetics", [])
        if phonetics:
            audio_link = phonetics[0].get("audio")

        meanings = entry.get("meanings", [])
        for meaning in meanings:
            definitions = meaning.get("definitions", [])
            for definition in definitions:
                example_sentence = definition.get("example")
                if example_sentence:
                    break
            if example_sentence:
                break
        
    return audio_link, example_sentence

def translate_and_update(row):
    english_word = row['English Word']
    translator = Translator()

    arabic_translation = translator.translate(english_word, dest='ar').text

    audio_link, example_sentence = get_audio_and_example(english_word)

    row['Arabic Translation'] = arabic_translation
    row['Audio Link'] = audio_link
    row['Example Sentence'] = example_sentence
    return row

if __name__ == "__main__":
    df = pd.read_excel('sample.xlsx')
    df = df.apply(translate_and_update, axis=1)
    df.to_excel('sample_translated.xlsx', index=False, engine='openpyxl')
