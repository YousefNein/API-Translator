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

if __name__ == "__main__":
    word_to_translate = input("Type the word you want to translate here in English:\n")
    audio_link, example_sentence = get_audio_and_example(word_to_translate)

    if audio_link:
        print(f"First Audio Link: {audio_link}")

    if example_sentence:
        print(f"First Example Sentence: {example_sentence}")
