import requests
from pprint import pprint
import json
import tkinter
import tkinter.ttk as ttk
import re
import random

r = requests.get('https://db.ygoprodeck.com/api/v5/cardsets.php')
result = json.loads(r.content.decode('utf-8'))
sets = [a["Set Name"] for a in result]
print(len(sets))
set2 = sets[34]
print(set2)

def get_n_random_cards(card_set, n):
    print(len(card_set))
    liste = random.sample(card_set, n)
    return liste

def create_deck_from_cardList(card_set):
    print(card_set)
    liste = [a["name"] for a in card_set]
    print(liste)

fenetre = tkinter.Tk()
fenetre.title('Draft deck generator')

set_list = ttk.Combobox(fenetre, values=sets)
set_list.pack ()

def generate () :                     # voir le chapitre sur les événements
    set_name = set_list.get()
    set_name = re.sub(" ", "%20", set_name).lower()
    r = requests.get(f'https://db.ygoprodeck.com/api/v5/cardinfo.php?set={set_name}')
    result = json.loads(r.content.decode('utf-8'))
    cards = get_n_random_cards(result, 30)
    create_deck_from_cardList(cards)

button = tkinter.Button (fenetre, text="Generate")
button.config (command = generate)
button.pack (side = tkinter.LEFT)

fenetre.mainloop()