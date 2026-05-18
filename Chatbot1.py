#Library
import random

print("-----SINTESIS BOT------")

###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai"], 
  "kabar": ["apa kabar?", "how are you?", "kabar kamu gimana?"],
  "ask": ["what is your name?", "nama kamu siapa?", "namamu siapa?"],
  "farewell": ["senang bertemu denganmu!", "dadah!", "goodbye", "bye"]
}
bot_dictionary = {
  "greeting": ["halo juga", "hi", "hello", "halooo"],
  "kabar": ["baik", "Kabar saya hari ini baik", "kabarku baik!"],
  "ask": ["nama aku Sinstesis", "my name is Sintesis", "nama saya Sintesis"],
  "farewell": ["senang bertemu denganmu juga!", "sampai bertemu lagi!", "see you!", "bye"]
}
#function
def greet_bot():
  out = random.choice(bot_dictionary["greeting"])
  return print(f"Sintesis: {out}")
def kabar_bot():
  hasil = random.choice(bot_dictionary["kabar"])
  return print(f"Sintesis: {hasil}")
def asking_bot():
  hasil = random.choice(bot_dictionary["ask"])
  return print(f"Sintesis: {hasil}")
def farewell_bot():
  hasil = random.choice(bot_dictionary["farewell"])
  return print(f"Sintesis: {hasil}")

while True:
  user = input("Kamu: ").lower()
  
  if user in dictionary["greeting"]:
    greet_bot()
  elif user in dictionary["kabar"]:
    kabar_bot()
  elif user in dictionary["ask"]:
    asking_bot()
  elif user in dictionary["farewell"]:
    farewell_bot()
  elif user == "exit":
    break
