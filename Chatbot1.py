#Library
import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time
#Design
console = Console()

console.print(
  Panel.fit(
    "[bold cyan]SINTESIS CHATBOT[/bold cyan]\n[green]by Azka Danish Kayana and Aida Rifdah Azizah[/green]",
    border_style="bright_blue"
  )
)

#func typing

def typing(teks):
  for huruf in teks:
    print(huruf, end="", flush=True)
    time.sleep(0.01)


#function teks
def sintesis(teks):
  console.print(
    f"[bold green]Sintesis: [/bold green]",
    end=""
  )
  typing(teks)
  print("")
def head_teks(teks):
  console.print(
    f"[bold bright_magenta]{teks}[/bold bright_magenta]\n",
    end=""
  )
  
def fitur_teks(teks):
  console.print(
    f"[bold blue]{teks}[/bold blue]\n",
    end=""
  )

def sintemath(teks):
  console.print(
    f"[bold green]Sintesis(Math): [/bold green]",
    end=""
  )
  typing(teks)
  print("")

def sintephysics(teks):
  console.print(
    f"[bold green]Sintesis(Physics): [/bold green]",
    end=""
  )
  typing(teks)
  print("")

def sinteflight(teks):
  console.print(
    f"[bold green]Sintesis(Flight): [/bold green]",
    end=""
  )
  typing(teks)
  print("")
###Dictionary
dictionary = {
  "greeting": ["hi", "halo", "hello", "hai", "yoo", "yow", "heloo", "helo", "hlo", "p", "yo", "yow", "yoww", "hii", "haii"], 
  "kabar": ["apa kabar?", "how are you?", "kabar kamu gimana?", "apakabar", "apa kabar"],
  "ask": ["what is your name?", "nama kamu siapa?", "namamu siapa?", 'nama kamu siapa', "namamu siapa", "what's your name"],
  "farewell": ["senang bertemu denganmu", "dadah", "goodbye", "bye", "dah", "see you"],
  "matematics": ["math", "math mode", "mode matematika", "matematika"],
  "sintecal": ["sintesis", "sinte", "sis", "sin", "tesis"],
  "help": ["help", "bantuan", "menu", "fitur", "daftar fitur"],
  "physics": ["physics", "physics mode", "fisika", "mode fisika"],
  "flight": ["flight", "flight mode", "penerbangan", "mode penerbangan"],
}
bot_dictionary = {
  "greeting": ["Halo juga!", "Hi!", "Hello!", "haloooo", "Yowww"],
  "kabar": ["Baik!", "Kabar saya hari ini baik", "Kabarku baik!"],
  "ask": ["Nama aku Sinstesis", "My name is Sintesis", "Nama saya Sintesis", "I'm Sintesis!"],
  "farewell": ["Senang bertemu denganmu juga!", "Sampai bertemu lagi!", "See you!", "Bye"],
  "sintecal": ["Sintesis disini!, ada yang bisa saya bantu?", "Ay ay ay, Sintesis siap membantu", "Siap tuan, ada yang bisa saya bantu", "Sintee--sis on!, can i help you?", "Sintesis here!, do you need help?"],
}
#help function
def help_menu():
  sintesis("")
  head_teks("Berikut daftar prompt yang bisa digunakan: \n")
  fitur_teks("- menu")
  fitur_teks("- math mode/mode matematika")
  fitur_teks("- physics mode/mode fisika")
  fitur_teks("- flight mode/mode penerbangan")
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
  fitur_teks("5. Exit Math Mode")

  ask_menu = Prompt.ask(
    "[bold green]Sintesis(Math): Pilih opsi: [/bold green]",
    choices=["1", "2", "3", "4", "5"]
  )

  ask_menu = int(ask_menu)
  
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
    sintemath(f"Hasilnya adalah {total_now}")
    time.sleep(1.5)
    math_bot()
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
    sintemath(f"Hasilnya adalah {total_now}")
    time.sleep(1.5)
    math_bot()
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
    sintemath(f"Hasilnya adalah {total_now}")
    time.sleep(1.5)
    math_bot()
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
        sintemath("Maaf angka pembagi tidak boleh 0!")
        break
      total.append(numin)
      total_now = total[0]
    else:
      for angka in total[1:]:
        total_now /= angka 
      sintemath(f"Hasilnya adalah {total_now}")
      time.sleep(1.5)
      math_bot()
  elif ask_menu == 5:
    sintemath("Keluar dari mode math.....")
  else:
    sintemath("Maaf anda salah memilih Opsi!")
#function physics
def physics_bot():
  sintesis("")
  head_teks("Pilih Opsi perhitungan Fisika berikut: \n")
  fitur_teks("1. Konversi waktu")
  fitur_teks("2. Konversi jarak")
  fitur_teks("3. Exit Physics Mode")

  ask_choice = Prompt.ask(
    "[bold green]Sintesis(Physics): Pilih opsi: [/bold green]",
    choices=["1", "2", "3"]
  )
  ask_choice = int(ask_choice)

  if ask_choice == 1:
    sintephysics("")
    head_teks("Pilih opsi konversi: \n")
    fitur_teks("1. Detik ke Menit")
    fitur_teks("2. Menit ke Jam")
    fitur_teks("3. Jam ke Menit")
    fitur_teks("4. Menit ke Detik")
    fitur_teks("5. Exit konversi Waktu")

    ask_time = Prompt.ask(
      "[bold green]Sintesis(Physics): Pilih opsi konversi waktu: [/bold green]",
      choices=["1", "2", "3", "4", "5"]
    )
    ask_time = int(ask_time)

    if ask_time == 1:
      detik = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green] Input detik: "
      ))
      menit = detik / 60
      hasil = f"{menit} menit"
      sintephysics(f"Hasil konversi {hasil}")
    
    elif ask_time == 2:
      menit = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green] Input menit: "
      ))
      jam = menit / 60
      hasil = f"{jam} jam"
      sintephysics(f"Hasil konversi {hasil}")
    
    elif ask_time == 3:
      jam = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green] Input jam: "
      ))
      menit = jam * 60
      hasil = f"{menit} menit"
      sintephysics(f"Hasil konversi {hasil}")
    
    elif ask_time == 4:
      menit = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input menit: "
      ))
      detik = menit * 60
      hasil = f"{detik} detik"
      sintephysics(f"Hasil Konversi {hasil}")

    elif ask_time == 5:
      sintephysics("Exit from konversi jarak...")
      physics_bot()
  
  elif ask_choice == 2:
    sintephysics("")
    head_teks("Pilih opsi konversi jarak: \n")
    fitur_teks("1. Meter ke Kilometer")
    fitur_teks("2. Kilometer ke Meter")
    fitur_teks("3. Exit konversi jarak")

    ask_distance = Prompt.ask(
      "[bold green]Sintesis(Physics): Pilih opsi: ",
      choices=["1", "2", "3"]
    )

    ask_distance = int(ask_distance)

    if ask_distance == 1:
      meter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Meter: "
      ))
      kilometer = meter / 1000
      hasil = f"{kilometer} km"
      sintephysics(f"Hasil konversi {hasil}")
    
    elif ask_distance == 2:
      kilometer = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kilometer: "
      ))
      meter = kilometer * 1000
      hasil = f"{meter} m"
      sintephysics(f"Hasil konversi {hasil}")
    
    elif ask_distance == 3:
      sintephysics("Exit from Konversi Jarak...")
      physics_bot()
  
  elif ask_choice == 3:
    sintephysics("Exiting Physics Mode..")

# Flight mode
def flight_bot():
  sinteflight("")
  head_teks("PILIH OPSI NEGARA\n")
  fitur_teks("1. Swiss")
  fitur_teks("2. Italy")
  fitur_teks("3. France")
  fitur_teks("4. Singapore")
  fitur_teks("5. Exit Flight Mode")

  ask_menu = Prompt.ask(
    "[bold green]Sintesis(Flight): Pilih opsi: [/bold green]",
    choices=["1", "2", "3", "4", "5"]
  )
  ask_menu = int(ask_menu)

  if ask_menu == 1:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 16000000
    hasil = f"Harga tiket ke Swiss untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    time.sleep(1.5)

  elif ask_menu == 2:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 15000000 
    hasil = f"Harga tiket ke Italy untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    time.sleep(1.5)

  elif ask_menu == 3:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 15000000 
    hasil = f"Harga tiket ke France untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    time.sleep(1.5)

  elif ask_menu == 4:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 5500000 
    hasil = f"Harga tiket ke Singapore untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    time.sleep(1.5)
    flight_bot()
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
def sintecal_bot():
  hasil = random.choice(bot_dictionary["sintecal"])
  return sintesis(hasil)
def matematics_bot():
  out = "Mode Matematika Aktif!"
  sintesis(out)
  math_bot()
def sintephysics_bot():
  hasil = "Physics mode Aktif!"
  sintesis(hasil)
  physics_bot()
def sinteflight_bot():
  out = "Flight mode Aktif!"
  sintesis(out)
  flight_bot()
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
  elif user in dictionary["sintecal"]:
    sintecal_bot()
  elif user in dictionary["matematics"]:
    matematics_bot()
  elif user in dictionary["help"]:
    help_menu()
  elif user in dictionary["physics"]:
    sintephysics_bot()
  elif user in dictionary["flight"]:
    sinteflight_bot()
  elif user in ["exit", "break"]:
    sintesis("Exiting.....")
    break
  else:
    sintesis("Maaf, saya tidak mengerti apa yang kamu maksud.")
