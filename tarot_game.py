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

print("Tarot game starting...")
sleep(2)
name = input("Welcome to this tarot game! What is your name? ")
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
i_card = input("Which card would you like to know more about? Please enter 1, 2, or 3: ")
i_card =-1
spread = [card1, card2, card3]
card = spread[i_card]
sleep(1)
print(f"You selected {card}!")
sleep(2)

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

tarot_meanings = {
 'The World': 'success, accomplishment, and fulfillment', 'Judgement': 'self-evaluation, awakening, decisiveness, forgiveness, and renewal',
 'The Sun': 'freedom, enthusiasm, confidence, happiness, and truth', 
 'The Moon': 'intuition, dreams, instability, misconception, and insecurity', 
 'The Star': 'inspiration, contentment, spirituality, and healing', 
 'The Tower': 'chaos, trauma, change, loss, violence, and inevitable endings',
 'The Devil': 'depression, obsession, dependendency, powerlessness, and cheating',
 'Temperance': 'balance, peace, moderation, tranquility, and soulmates', 
 'Death': 'new beginnings, letting go, transition, and change', 
 'The Hanged Man': 'confinement, uncertainty, lack of direction, and letting go', 
 'Justice': 'karmic justice, consequences, law, truth, and integrity', 
 'The Wheel of Fortune': 'good luck, destiny, soulmates, chance, fate, and fortune', 
 'The Hermit': 'spiritual enlightenment, soul searching, self reflection, and solitude', 
 'Strength': 'courage, bravery, confidence, compassion, and overcoming self doubt', 
 'The Chariot': 'victory, success, ambition, hard work, self-discipline, and focus', 
 'The Lovers': 'love, soulmates, partnerships, romance, desire, and shared values', 
 'The Hierophant': 'traditional values, conventional, conformity, commitment, religion, and beliefs', 
 'The Emperor': 'stability, dependability, fatherhood, authority, and protectiveness', 
 'The Empress': 'pregnancy, motherhood, sensuality, beauty, femininity, nature, and art', 
 'The High Priestess': 'desirability, mystery, spirituality, fertility, and unattainability', 
 'The Magician': 'power, influence, willpower, resourcefulness, skill, logic, and concentration', 
 'The Fool': 'innocence, freedom, carelessness, idealism, youth, and new beginnings', 
 'The World - Reversed': 'stagnation, disappoinment, burden, and lack of achievement', 
 'Judgement - Reversed': 'self-doubt, lack of self-awareness, unfair blame, and false accusations', 
 'The Sun - Reversed': 'lack of enthusiasm, sadness, pessimism, ego, and conceitedness', 
 'The Moon - Reversed': 'releasing fear, subsiding anxiety, truth, and blocked intuition', 
 'The Star - Reversed': 'hopelessness, despair, boredom, and monotony', 
 'The Tower - Reversed': 'resisting change, avoiding tragedy, avoiding loss, and codependence', 
 'The Devil - Reversed': 'detachment, independence, overcoming addiction, freedom, and revelation', 
 'Temperance - Reversed': 'imbalance, excess, clashing, lack of perspective, and antagonism', 
 'Death - Reversed': 'inability to move forward, fear of beginnings, resisting change, and dependency', 
 'The Hanged Man - Reversed': 'discontentment, apathy, disinterest, stagnation, and detachment', 
 'Justice - Reversed': 'injustice, dishonesty, corruption, unfairness, and karmic avoidance', 
 'The Wheel of Fortune - Reversed': 'bad luck, upheavel, disorder, disruption, and delays', 
 'The Hermit - Reversed': 'loneliness, paranoia, isolation, withdrawal, and reclusive', 
 'Strength - Reversed': 'vulnerability, weakness, lack of confidence, and low self-esteem', 
 'The Chariot - Reversed': 'lack of direction, lack of self-control, forcefulness, and coercion', 
 'The Lovers - Reversed': 'disharmony, imbalance, conflict, detachment, and disconnection', 
 'The Hierophant - Reversed': 'challenging tradition, reversed roles, and non-conformity', 
 'The Emperor - Reversed': 'abuse of power, excessively controlling, stubbornnes, lack of disciple, and rigidity', 
 'The Empress - Reversed': 'insecurity, overbearingness, disharmony, and negligence', 
 'The High Priestess - Reversed': 'unwanted attention, lack of self-belief, and repression of intuition', 
 'The Magician - Reversed': 'manipulation, greed, untrustworthiness, cunning, and lack of mental clarity', 
 'The Fool - Reversed': 'recklessness, negligence, distraction, apathy, and irrationality'
 }

sleep(2)
card_meaning = tarot_meanings.get(card)
print(f"{card} represents {card_meaning}.")