import requests
import json
import tkinter
import tkinter.ttk as ttk
import re
import random

r = requests.get('https://db.ygoprodeck.com/api/v6/cardsets.php')
result = json.loads(r.content.decode('utf-8'))
sets = [a["set_name"] for a in result]

def get_random_cards(card_set, n, set_name):
    #Divide the card set into the common set and other set
    common_cards = []
    other_cards = []
    for card in card_set:
        for edition in card["card_sets"]:
            if edition["set_name"]==set_name:
                if edition["set_rarity"] == "Common":
                    common_cards.append(card["id"])
                else:
                    other_cards.append(card["id"])
                break

    #Open n boosters
    cards_list = []
    if len(common_cards)!=0:
        for i in range(n):
            for card_id in random.choices(common_cards, k=8):
                cards_list.append(card_id)
            for card_id in random.choices(other_cards, k=1):
                cards_list.append(card_id)
    else:
        for i in range(n):
            for card_id in random.choices(other_cards, k=9):
                cards_list.append(card_id)
    return cards_list

def create_deck_from_cardList(card_set):
    with open("deck.ydk", "w") as f:  
        f.write("#main\n")
        print(card_set)
        for card in card_set:
            f.write(str(card))
            f.write("\n")

fenetre = tkinter.Tk()
fenetre.title('Draft deck generator')
fenetre.configure(background='#3E4149')

set_list = ttk.Combobox(fenetre, values=sets)
set_list.pack ()

def generate():
    #Get the name of the booster, and the quantity of boosters
    set_name = set_list.get()
    nb_booster = scaller.get()

    #Escape the spaces
    request_set_name = re.sub(" ", "%20", set_name).lower()

    #API request : get the cards
    r = requests.get(f'https://db.ygoprodeck.com/api/v6/cardinfo.php?set={request_set_name}')
    result = json.loads(r.content.decode('utf-8'))

    #Open virtual boosters
    cards = get_random_cards(result, nb_booster, set_name)
    create_deck_from_cardList(cards)

scaller = tkinter.Scale(fenetre, orient='horizontal', from_=1, to=20,
      resolution=1, tickinterval=1, length=350,
      label='Nombre de booster')
scaller.pack ()


button = tkinter.Button (fenetre, text="Generate", highlightbackground='#3E4149')
button.config (command = generate)
button.pack ()


fenetre.mainloop()