#Library
import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

#Design
console = Console()

console.print(
  Panel.fit(
    "[bold cyan]SINTESIS CHATBOT[/bold cyan]\n[green]by Azka Danish Kayana[/green]",
    border_style="bright_blue"
  )
)
#function teks
def sintesis(teks):
  console.print(
    f"[bold green]Sintesis: [/bold green]{teks}\n",
    end=""
  )
def head_teks(teks):
  console.print(
    f"[bold bright_magenta]{teks}[/bold bright_magenta]\n",
    end=""
  )
def fitur_teks(teks):
  console.print(
    f"[blue_bright]{teks}[/blue_bright]\n",
    end=""
  )

###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai", "yoo", "yow", "heloo", "helo", "hlo", "p", "yo", "yow", "yoww", "hii", "haii"], 
  "kabar": ["apa kabar?", "how are you?", "kabar kamu gimana?", "apakabar", "apa kabar"],
  "ask": ["what is your name?", "nama kamu siapa?", "namamu siapa?", 'nama kamu siapa', "namamu siapa", "what's your name"],
  "farewell": ["senang bertemu denganmu", "dadah", "goodbye", "bye", "dah"],
  "matematics": ["math", "math mode", "mode matematika", "matematika", "matematika"],
  "sintecal": ["sintesis", "sinte", "sis", "sin", "tesis"],
  "help": ["help", "bantuan", "menu", "fitur", "daftar fitur"]
}
bot_dictionary = {
  "greeting": ["Halo juga!", "Hi!", "Hello!", "haloooo", "Yowww"],
  "kabar": ["Baik!", "Kabar saya hari ini baik", "Kabarku baik!"],
  "ask": ["Nama aku Sinstesis", "My name is Sintesis", "Nama saya Sintesis", "I'm Sintesis!"],
  "farewell": ["Senang bertemu denganmu juga!", "Sampai bertemu lagi!", "See you!", "Bye"],
  "sintecal": ["Sintesis disini!, ada yang bisa saya bantu?", "Ay ay ay, Sintesis siap membantu", "Siap tuan, ada yang bisa saya bantu", "Sintee--sis on!, can i help you?", "Sintesis here!, do you need help?"],
}
#help function
def help():
  sintesis("")
  head_teks("Berikut daftar prompt yang bisa digunakan: \n")
  fitur_teks("- menu")
  fitur_teks("- math mode/mode matematika")
  fitur_teks("- exit/break (Keluar dari program)")
#math mode
def math_bot():
  console.print(
    "[bold green]Sintesis(Math):[/bold green]\n"
  )
  head_teks("PILIH OPSI BERIKUT!\n")
  fitur_teks("1. + (Pertambahan)")
  fitur_teks("2. - (Pengurangan)")
  fitur_teks("3. x (Perkalian)")
  fitur_teks("4. / (Pembagian)")
  fitur_teks("5. Exit (Keluar mode)")

  ask_menu = int(Prompt.ask(
    "[bold green]Sintesis(Math): Pilih opsi: [/bold green]",
  ))
  if ask_menu == 1:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Math): [/bold green]Menambah berapa angka? "
      ))
    total = []
    for i in range(total_in):
      numin = float(Prompt.ask(
        f"[bold green]Input Angka {i+1}: [/bold green]"
      ))
      total.append(numin)
    total_now = sum(total)
    console.print(
      f"[bold green]Sintesis(Math): [/bold green]Hasilnya adalah {total_now}"
    ) 
  elif ask_menu == 2:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Math): Mengurangi berapa angka? [/bold green]"
    ))
    total = []
    for i in range(total_in):
      numin = float(Prompt.ask(
        f"[bold green]Input Angka {i+1}: [/bold green]"
      ))
      total.append(numin)
    total_now = total[0]
    for angka in total[1:]:
      total_now -= angka 
    console.print(
      f"[bold green]Sintesis(Math): Hasilnya adalah[/bold green] {total_now}"
    )
  elif ask_menu == 3:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Math): Mengkali berapa angka? [/bold green]"
    ))
    total = []
    for i in range(total_in):
      numin = float(Prompt.ask(
        f"[bold green]Input Angka {i+1}: [/bold green]"
      ))
      total.append(numin)
      total_now = total[0]
    for angka in total[1:]:
      total_now *= angka
    console.print(
      f"[bold green]Sintesis(Math): Hasilnya adalah[/bold green] {total_now}"
    )
  elif ask_menu == 4:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Math): Membagi berapa angka? [/bold green]"
    ))
    total = []
    for i in range(total_in):
      numin = float(Prompt.ask(
        f"[bold green]Input Angka {i+1}: [/bold green]"
      ))
      if i > 0 and numin == 0:
        console.print(
          "[bold green]Sintesis(Math): [/bold green]Maaf angka pembagi tidak boleh 0!"
        )
        break
      total.append(numin)
      total_now = total[0]
    else:
      for angka in total[1:]:
        total_now /= angka 
      console.print(
        f"[bold green]Sintesis(Math): Hasilnya adalah[/bold green] {total_now}"
      )
  elif ask_menu == 5:
    console.print(
      "[bold green]Sintesis(Math):[/bold green] Keluar dari mode math....."
    )
  else:
    console.print("[bold green]Sintesis:[/bold green] Maaf anda salah memilih Opsi!")
#function jawaban
def greet_bot():
  hasil = random.choice(bot_dictionary["greeting"])
  return sintesis(hasil)
def kabar_bot():
  hasil = random.choice(bot_dictionary["kabar"])
  return sintesis(hasil)
def asking_bot():
  hasil = random.choice(bot_dictionary["ask"])
  return sintesis(hasil)
def farewell_bot():
  hasil = random.choice(bot_dictionary["farewell"])
  return sintesis(hasil)
def matematics_bot():
  out = "Mode Matematika Aktif!"
  sintesis(out)
  math_bot()
def sintecal_bot():
  hasil = random.choice(bot_dictionary["sintecal"])
  sintesis(hasil)
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
  elif user in dictionary["help"]:
    help()
  elif user in ["exit", "break"]:
    sintesis("Exiting.....")
    break
  else:
    sintesis("Maaf, saya tidak mengerti apa yang kamu maksud.")
