import random as rd
from time import sleep

tarot = ["The World", "Judgement", "The Sun", "The Moon", "The Star", "The Tower", 
              "The Devil", "Temperance", "Death", "The Hanged Man", "Justice", 
              "The Wheel of Fortune", "The Hermit", "Strength", "The Chariot", "The Lovers", 
              "The Hierophant", "The Emperor", "The Empress", "The High Priestess", 
              "The Magician", "The Fool"]

reversed_deck = []
for card in tarot:
    card += " - Reversed"
    reversed_deck.append(card)
    
tarot_deck = tarot + reversed_deck
print(tarot_deck)

print("Tarot game starting...")
sleep(2)
name = input("Welcome to this tarot game! What is your name? ")
sleep(1)
print(f"Hi, {name}.")
sleep(0.5)
print("Shuffling the deck...")
sleep(2)

i = rd.randint(0, len(tarot_deck))
i2 = rd.randint(0, len(tarot_deck))
i3 = rd.randint(0, len(tarot_deck))

card1 = tarot_deck[i]
card2 = tarot_deck[i2]
card3 = tarot_deck[i3]

print(f"Three cards were pulled: {card1}, {card2}, and {card3}.")
sleep(1)
i_card = input("Which card would you like to know more about? Please enter 1, 2, or 3:")
i_card =-1
spread = [card1, card2, card3]
card = spread[i_card]

print(f"You selected {card}!")

['The World', 'Judgement', 'The Sun', 'The Moon', 'The Star', 'The Tower', 'The Devil', 
 'Temperance', 'Death', 'The Hanged Man', 'Justice', 'The Wheel of Fortune', 'The Hermit', 
 'Strength', 'The Chariot', 'The Lovers', 'The Hierophant', 'The Emperor', 'The Empress', 
 'The High Priestess', 'The Magician', 'The Fool', 'The World - Reversed', 
 'Judgement - Reversed', 'The Sun - Reversed', 'The Moon - Reversed', 'The Star - Reversed', 
 'The Tower - Reversed', 'The Devil - Reversed', 'Temperance - Reversed', 'Death - Reversed', 
 'The Hanged Man - Reversed', 'Justice - Reversed', 'The Wheel of Fortune - Reversed', 
 'The Hermit - Reversed', 'Strength - Reversed', 'The Chariot - Reversed', 
 'The Lovers - Reversed', 'The Hierophant - Reversed', 'The Emperor - Reversed', 
 'The Empress - Reversed', 'The High Priestess - Reversed', 'The Magician - Reversed', 
 'The Fool - Reversed']

tarot_meanings = {'The World': 'success, accomplishment, and fulfillment', 'Judgement': 'self-evaluation, awakening, decisiveness, forgiveness, and renewal',
'The Sun': 'freedom, enthusiasm, confidence, happiness, and truth', 
'The Moon': 'intuition, dreams, instability, misconception, and insecurity', 
'The Star': 'inspiration, contentment, spirituality, and healing', 
'The Tower': 'chaos, trauma, change, loss, violence, and inevitable endings',
'The Devil', 
'Temperance', 
'Death', 
'The Hanged Man', 
'Justice', 
'The Wheel of Fortune', 
'The Hermit', 
 'Strength', 
 'The Chariot', 
 'The Lovers', 
 'The Hierophant', 
 'The Emperor', 
 'The Empress', 
 'The High Priestess', 
 'The Magician', 
 'The Fool', 
 'The World - Reversed', 
 'Judgement - Reversed', 
 'The Sun - Reversed', 
 'The Moon - Reversed', 
 'The Star - Reversed', 
 'The Tower - Reversed', 
 'The Devil - Reversed', 
 'Temperance - Reversed', 
 'Death - Reversed', 
 'The Hanged Man - Reversed', 
 'Justice - Reversed', 
 'The Wheel of Fortune - Reversed', 
 'The Hermit - Reversed', 
 'Strength - Reversed', 
 'The Chariot - Reversed', 
 'The Lovers - Reversed', 
 'The Hierophant - Reversed', 
 'The Emperor - Reversed', 
 'The Empress - Reversed', 
 'The High Priestess - Reversed', 
 'The Magician - Reversed', 
 'The Fool - Reversed'}

