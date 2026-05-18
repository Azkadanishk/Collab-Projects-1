#Library
import random

###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai"], 
}
bot_dictionary = {
  "greeting": ["Halo juga", "Hi", "Hello", "Halooo"]
}
#function
def greet_bot():
  out = random.choice(dictionary["greeting"])
  return print(f"Sintesis: {out}")

while True:
  user = input("Kamu: ").lower()
  
  if user in dictionary["greeting"]:
    greet_bot()

  elif user == "exit":
    break
