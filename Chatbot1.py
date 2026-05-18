#Library
import random

#Design
print("-----SINTESIS BOT------")

###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai", "yoo", "yow", "heloo"], 
  "kabar": ["apa kabar?", "how are you?", "kabar kamu gimana?", "apakabar", "apa kabar"],
  "ask": ["what is your name?", "nama kamu siapa?", "namamu siapa?", 'nama kamu siapa', "namamu siapa", "what's your name"],
  "farewell": ["senang bertemu denganmu", "dadah", "goodbye", "bye", "dah"]
}
bot_dictionary = {
  "greeting": ["Halo juga!", "Hi!", "Hello!", "haloooo", "Yowww"],
  "kabar": ["Baik!", "Kabar saya hari ini baik", "Kabarku baik!"],
  "ask": ["Nama aku Sinstesis", "My name is Sintesis", "Nama saya Sintesis"],
  "farewell": ["Senang bertemu denganmu juga!", "Sampai bertemu lagi!", "See you!", "Bye"]
}
#function
def greet_bot():
  hasil = random.choice(bot_dictionary["greeting"])
  return print(f"Sintesis: {hasil}")
def kabar_bot():
  hasil = random.choice(bot_dictionary["kabar"])
  return print(f"Sintesis: {hasil}")
def asking_bot():
  hasil = random.choice(bot_dictionary["ask"])
  return print(f"Sintesis: {hasil}")
def farewell_bot():
  hasil = random.choice(bot_dictionary["farewell"])
  return print(f"Sintesis: {hasil}")

#math mode
def math_bot():
  print("PILIH OPSI BERIKUT!\n")
  print("1. + (Pertambahan)\n")
  print("2. - (Pengurangan)\n")
  print("3. x (Perkalian)\n")
  print("4. / (Pembagian)\n")
  print("5. Exit (Keluar mode)")

  ask_menu = int(input("Sintesis: Pilih opsi: "))
  if ask_menu == 1:
    total_in = int(input("Sintesis(Math): Menambah berapa angka?"))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      total.append(numin)
    total_now = sum(total)
    print(f"Sintesis(Math): Hasilnya adalah {total_now}")
  elif ask_menu == 2:
    total_in = int(input("Sintesis(Math): Mengurangi berapa angka?"))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      total.append(numin)
    total_now = total[0]
    for angka in total[1:]:
      total_now -= angka 
    print(f"Sintesis(Math): Hasilnya adalah {total_now}")

while True:
  #User setting
  user = input("Kamu: ").lower()
  
  #distribusi function
  if user in dictionary["greeting"]:
    greet_bot()
  elif user in dictionary["kabar"]:
    kabar_bot()
  elif user in dictionary["ask"]:
    asking_bot()
  elif user in dictionary["farewell"]:
    farewell_bot()
    break
  elif user == "matematika":
    math_bot()
  elif user == "exit":
    print("Sintesis: Exiting.....")
    break
