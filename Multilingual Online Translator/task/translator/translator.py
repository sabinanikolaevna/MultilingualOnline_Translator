import requests
import bs4
from bs4 import BeautifulSoup
import sys
args = sys.argv
l1 = args[1]
l2 = args[2]
word = args[3]
languages = {'1': 'Arabic', '2': "German", '3': 'English', '4': 'Spanish', '5': "French", '6': "Hebrew", '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese', '11': 'Romanian', '12': 'Russian', '13': 'Turkish'}
supported = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']
def single_language():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://context.reverso.net/translation/{l1.lower()}-{l2.lower()}/{word}'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Something wrong with your internet connection")
    elif response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        words = soup.find_all('a', {'class': 'translation'})
        words = [word.text.strip() for word in words[1:]]
        sentences = soup.find(id='examples-content').find_all('span', {'class': 'text'})
        sentences = [sentence.text.strip() for sentence in sentences]
        phrase = f"{l2} Translations:"
        saved_word = words[0]
        phrase2 = f"{l2} Example:"
        saved_sentence = sentences[0]
        saved_sentence2 = sentences[1]
        file = open(f'{word}.txt', 'a')
        file.write(phrase + '\n')
        file.write(saved_word + '\n')
        file.write(phrase2 + '\n')
        file.write(saved_sentence + '\n')
        file.write(saved_sentence2 + '\n')
        file.close()
        print(phrase)
        print(saved_word)
        print(phrase2)
        print(saved_sentence)
        print(saved_sentence2)

def all_languages():
    for i in languages:
        if languages[i].lower() == l1:
            pass
        else:
            l2 = languages[i]
            headers = {'User-Agent': 'Mozilla/5.0'}
            url = f'https://context.reverso.net/translation/{l1.lower()}-{l2.lower()}/{word}'
            response = requests.get(url, headers=headers)
            if response.status_code == 404:
                print(f"Sorry, unable to find {word}")
                break
            elif response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                words = soup.find_all('a', {'class': 'translation'})
                words = [word.text.strip() for word in words[1:]]
                sentences = soup.find(id='examples-content').find_all('span', {'class': 'text'})
                sentences = [sentence.text.strip() for sentence in sentences]
                phrase = f"{l2} Translations:"
                saved_word = words[0]
                phrase2 = f"{l2} Example:"
                saved_sentence = sentences[0]
                saved_sentence2 = sentences[1]
                file = open(f'{word}.txt', 'a')
                file.write(phrase + '\n')
                file.write(saved_word + '\n')
                file.write(phrase2 + '\n')
                file.write(saved_sentence + '\n')
                file.write(saved_sentence2 + '\n')
                file.close()
                print(phrase)
                print(saved_word)
                print(phrase2)
                print(saved_sentence)
                print(saved_sentence2)


if l1 not in supported:
    print(f"Sorry, the program doesn't support {l1}")
elif l2 not in supported and l2 != 'all':
    print(f"Sorry, the program doesn't support {l2}")
elif l2 != 'all':
    single_language()
elif l2 == 'all':
    all_languages()
