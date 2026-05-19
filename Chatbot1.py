#Library
import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
import time

#Design
console = Console()

console.print(
  Panel.fit(
    "[bold cyan]SINTESIS CHATBOT[/bold cyan]\n[green]by Azka Danish Kayana and Aida Rifdah Azizah[/green]",
    border_style="bright_blue"
  )
)


###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai", "yoo", "yow", "heloo"], 
  "kabar": ["apa kabar?", "how are you?", "kabar kamu gimana?", "apakabar", "apa kabar"],
  "ask": ["what is your name?", "nama kamu siapa?", "namamu siapa?", 'nama kamu siapa', "namamu siapa", "what's your name"],
  "farewell": ["senang bertemu denganmu", "dadah", "goodbye", "bye", "dah"],
  "matematics": ["math", "math mode", "mode matematika", "matematika", "matematika"]
}
bot_dictionary = {
  "greeting": ["Halo juga!", "Hi!", "Hello!", "haloooo", "Yowww"],
  "kabar": ["Baik!", "Kabar saya hari ini baik", "Kabarku baik!"],
  "ask": ["Nama aku Sinstesis", "My name is Sintesis", "Nama saya Sintesis"],
  "farewell": ["Senang bertemu denganmu juga!", "Sampai bertemu lagi!", "See you!", "Bye"]
}
#math mode
def math_bot():
  print("Sintesis: ")
  print("PILIH OPSI BERIKUT!\n")
  print("1. + (Pertambahan)")
  print("2. - (Pengurangan)")
  print("3. x (Perkalian)")
  print("4. / (Pembagian)")
  print("5. Exit (Keluar mode)")

  ask_menu = int(input("Sintesis: Pilih opsi: "))
  if ask_menu == 1:
    total_in = int(input("Sintesis(Math): Menambah berapa angka? "))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      total.append(numin)
    total_now = sum(total)
    print(f"Sintesis(Math): Hasilnya adalah {total_now}")
  elif ask_menu == 2:
    total_in = int(input("Sintesis(Math): Mengurangi berapa angka? "))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      total.append(numin)
    total_now = total[0]
    for angka in total[1:]:
      total_now -= angka 
    print(f"Sintesis(Math): Hasilnya adalah {total_now}")
  elif ask_menu == 3:
    total_in = int(input("Sintesis(Math): Mengkali berapa angka? "))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      total.append(numin)
      total_now = total[0]
    for angka in total[1:]:
      total_now *= angka
    print(f"Sintesis(Math): Hasilnya adalah {total_now}")
  elif ask_menu == 4:
    total_in = int(input("Sintesis(Math): Membagi berapa angka? "))
    total = []
    for i in range(total_in):
      numin = float(input(f"Input Angka {i+1}: "))
      if i > 0 and numin == 0:
        print("Sintesis: Maaf angka pembagi tidak boleh 0!")
        break
      total.append(numin)
      total_now = total[0]
    else:
      for angka in total[1:]:
        total_now /= angka 
      print(f"Sintesis(Math): Hasilnya adalah {total_now}")
  elif ask_menu == 5:
    print("Sintesis(Math): Keluar dari mode math.....")
  else:
    print("Sintesis: Maaf anda salah memilih Opsi!")
#function jawaban
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
def matematics_bot():
  print("Sintesis: Mode Matematika Aktif!")
  math_bot()
    

#Interface user set
while True:
  #User setting
  user = Prompt.ask(
    "[bold yellow]kamu[/bold yellow]"
  ).lower()
  
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
  elif user in dictionary["matematics"]:
    matematics_bot()
  elif user in ["exit", "break"]:
    print("Sintesis: Exiting.....")
    break
