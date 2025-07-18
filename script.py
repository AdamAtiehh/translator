from translate import Translator

T_dict = {
    'es': 'Spanish',
    'pt': 'Portuguese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese'
}

print("Available Languages:")
for key, lang in T_dict.items():
    print(f"{key} → {lang}")

while True:
    lang_input = input("Choose a language code: ").strip().lower()
    if lang_input in T_dict:
        break
    else:
        print("Invalid language code")

translator = Translator(to_lang=lang_input)

word = input("Enter the word you want to translate: ").strip()

try:
    translated = translator.translate(word)
    print(f"-> {translated}")
except Exception as e:
    print(f"Translation failed: {e}")

try:
    with open('./Translation.txt',mode='a') as my_file:
        text=my_file.write(f'{word} : {translated} \n')
        print('Saved in a txt file')
except FileNotFoundError as err:
    print('Not able to save to File')
    raise err
except IOError as err:
    print('Something went Wrong')
    raise err