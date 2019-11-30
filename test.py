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
set2 = re.sub(" ", "%20", set2).lower()
r = requests.get(f'https://db.ygoprodeck.com/api/v5/cardinfo.php?set={set2}')
result = json.loads(r.content.decode('utf-8'))
print(result[0])
cards = [a["name"] for a in result]
print(len(cards))

def get_n_random_cards(card_set, n):
    liste = random.sample(card_set, n)
    return liste

def create_deck_from_cardList(card_set):
    
    return()

fenetre = tkinter.Tk()
fenetre.title('Draft deck generator')

set_list = ttk.Combobox(fenetre, values=sets)
set_list.pack ()

def print_file () :                     # voir le chapitre sur les événements
    print(set_list.get())

button = tkinter.Button (fenetre, text="Generate")
button.config (command = print_file)
button.pack (side = tkinter.LEFT)

fenetre.mainloop()