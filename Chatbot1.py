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

#function loop fitur utama

def loop_feature(feature):
  question = Prompt.ask(
    "[bold red]Next y/n? [/bold red]"
  )
  if question == "y":
    feature()
  elif question == "n":
    feature()
  else:
    feature()
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
  "thank": ["terimakasih", "terima kasih", "makasih", "mekasih", "mksh", "thanks", "thank you", "thankyou", "thx"]
}
bot_dictionary = {
  "greeting": ["Halo juga!", "Hi!", "Hello!", "haloooo", "Yowww"],
  "kabar": ["Baik!", "Kabar saya hari ini baik", "Kabarku baik!"],
  "ask": ["Nama aku Sinstesis", "My name is Sintesis", "Nama saya Sintesis", "I'm Sintesis!"],
  "farewell": ["Senang bertemu denganmu juga!", "Sampai bertemu lagi!", "See you!", "Bye"],
  "sintecal": ["Sintesis disini!, ada yang bisa saya bantu?", "Ay ay ay, Sintesis siap membantu", "Siap tuan, ada yang bisa saya bantu", "Sintee--sis on!, can i help you?", "Sintesis here!, do you need help?"],
  "thank": ["Sama-sama!", "Tentu, senang bisa membantu!", "You're welcome!", "Sama-sama, senang bisa membantu!"]
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
    loop_feature(math_bot)
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
    loop_feature(math_bot)
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
    loop_feature(math_bot)
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
      loop_feature(math_bot)
  elif ask_menu == 5:
    sintemath("Exiting Math Mode...")
  else:
    sintemath("Maaf anda salah memilih Opsi!")
#function physics
def physics_bot():
  sintesis("")
  head_teks("Pilih Opsi perhitungan Fisika berikut: \n")
  fitur_teks("1. Konversi waktu")
  fitur_teks("2. Konversi jarak")
  fitur_teks("3. Konversi Suhu")
  fitur_teks("4. Kecepatan")
  fitur_teks("5. Energi")
  fitur_teks("6. Exit Physics Mode")

  ask_choice = Prompt.ask(
    "[bold green]Sintesis(Physics): Pilih opsi: [/bold green]",
    choices=["1", "2", "3", "4", "5", "6"]
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
      loop_feature(physics_bot)

    elif ask_time == 2:
      menit = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green] Input menit: "
      ))
      jam = menit / 60
      hasil = f"{jam} jam"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)
    
    elif ask_time == 3:
      jam = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green] Input jam: "
      ))
      menit = jam * 60
      hasil = f"{menit} menit"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)
    
    elif ask_time == 4:
      menit = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input menit: "
      ))
      detik = menit * 60
      hasil = f"{detik} detik"
      sintephysics(f"Hasil Konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_time == 5:
      sintephysics("Exit from konversi jarak...")
      physics_bot()
  
  elif ask_choice == 2:
    sintephysics("")
    head_teks("Pilih opsi konversi jarak: \n")
    fitur_teks("1. Meter ke Kilometer")
    fitur_teks("2. Kilometer ke Meter")
    fitur_teks("3. Milimeter ke Centimeter")
    fitur_teks("4. Centimeter ke Desimeter")
    fitur_teks("5. Desimeter ke Meter")
    fitur_teks("6. Meter ke Dekameter")
    fitur_teks("7. Dekameter ke Hektometer")
    fitur_teks("8. Hektometer ke Kilometer")
    fitur_teks("9. Kilometer ke Hektometer")
    fitur_teks("10. Hektometer ke Dekameter")
    fitur_teks("11. Dekameter ke Meter")
    fitur_teks("12. Meter ke Desimeter")
    fitur_teks("13. Desimeter ke Centimeter")
    fitur_teks("14. Centimeter ke Milimeter")
    fitur_teks("15. Exit konversi jarak")

    ask_distance = Prompt.ask(
      "[bold green]Sintesis(Physics): Pilih opsi: ",
      choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    )

    ask_distance = int(ask_distance)

    if ask_distance == 1:
      meter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Meter(m): "
      ))
      kilometer = meter / 1000
      hasil = f"{kilometer} km"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)
    
    elif ask_distance == 2:
      kilometer = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kilometer(km): "
      ))
      meter = kilometer * 1000
      hasil = f"{meter} m"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 3:
      milimeter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Milimeter(mm): "
      ))
      centimeter = milimeter / 10
      hasil = f"{centimeter} cm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 4:
      centimeter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Centimeter(cm): "
      ))
      desimeter = centimeter / 10
      hasil = f"{desimeter} dm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 5:
      desimeter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Desimeter(dm): "
      ))
      meter = desimeter / 10
      hasil = f"{meter} m"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 6:
      meter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Meter(m): "
      ))
      dekameter = meter / 10
      hasil = f"{dekameter} dam"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 7:
      dekameter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Dekameter(dam): "
      ))
      hektometer = dekameter / 10
      hasil = f"{hektometer} hm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 8:
      hektometer = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Hektometer(hm): "
      ))
      kilometer = hektometer / 10
      hasil = f"{kilometer} km"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 9:
      kilometer = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kilometer(km): "
      ))
      hektometer = kilometer * 10
      hasil = f"{hektometer} hm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 10:
      hektometer = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Hektometer(hm): "
      ))
      dekameter = hektometer * 10
      hasil = f"{dekameter} dam"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 11:
      dekameter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Dekameter(dam): "
      ))
      meter = dekameter * 10
      hasil = f"{meter} m"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 12:
      meter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input meter(m): "
      ))
      desimeter = meter * 10
      hasil = f"{desimeter} dm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 13:
      desimeter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input desimeter(dm): "
      ))
      centimeter = desimeter * 10
      hasil = f"{centimeter} cm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 14:
      centimeter = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Centimeter(cm): "
      ))
      milimeter = centimeter * 10
      hasil = f"{milimeter} mm"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_distance == 15:
      sintephysics("Exit from Konversi Jarak...")
      physics_bot()
  
  elif ask_choice == 3:
    sintephysics("")
    head_teks("Pilih opsi konversi suhu: \n")
    fitur_teks("1. Celcius ke Reamur")
    fitur_teks("2. Reamur ke Celcius")
    fitur_teks("3. Celcius ke Fahrenheit")
    fitur_teks("4. Fahrenheit ke Celcius")
    fitur_teks("5. Celcius ke Kelvin")
    fitur_teks("6. Exit konversi Suhu")

    ask_suhu = Prompt.ask(
      "[bold green]Sintesis(Physics): Pilih opsi: ",
      choices=["1", "2", "3", "4", "5", "6"]
    )

    ask_suhu = int(ask_suhu)

    if ask_suhu == 1:
      celcius = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Celcius(°C): "
      ))
      reamur = (4/5) * celcius
      hasil = f"{reamur} °R"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot)

    elif ask_suhu == 2:
      reamur = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Reamur(°R): "
      ))
      celcius = (5/4) * reamur
      hasil = f"{celcius} °C"
      sintephysics(f"Hasil konversi {hasil}")  
      loop_feature(physics_bot) 

    elif ask_suhu == 3:
      celcius = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Celcius(°C): "
      ))
      fahrenheit = (9/5) * celcius + 32
      hasil = f"{fahrenheit} °F"
      sintephysics(f"Hasil konversi {hasil}")
      loop_feature(physics_bot) 

    elif ask_suhu == 4:
      fahrenheit = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Fahrenheit(°F): "
      ))
      celcius = (5/9) * (fahrenheit - 32)
      hasil = f"{celcius} °C"
      sintephysics(f"Hasil konversi {hasil}")  
      loop_feature(physics_bot) 

    elif ask_suhu == 5:
      celcius = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Celcius(°C): "
      ))
      kelvin = celcius + 273
      hasil = f"{kelvin} K"
      sintephysics(f"Hasil konversi {hasil}") 
      loop_feature(physics_bot)

    elif ask_suhu == 6:
      sintephysics("Exiting Konversi Suhu...")  
      physics_bot()

  elif ask_choice == 4:
    sintephysics("")
    head_teks("Pilih opsi berikut: ")
    fitur_teks("1. Kecepatan(v)")
    fitur_teks("2. Jarak(s)")
    fitur_teks("3. Waktu(t)")
    fitur_teks("4. Exit Kecepatan")

    ask_speed = Prompt.ask(
      "[bold green]Sintesis(Physics): [/bold green]Pilih Opsi: ",
      choices=["1", "2", "3", "4"]
    )
    
    ask_speed = int(ask_speed)

    if ask_speed == 1:
      jarak = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Jarak(m): "
      ))
      waktu = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Waktu(t): "
      ))
      kecepatan = jarak / waktu
      hasil = f"{kecepatan} m/s"
      sintephysics(f"Hasil perhitungan Kecepatan adalah {hasil}")
      loop_feature(physics_bot)

    elif ask_speed == 2:
      kecepatan = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kecepatan(m/s): "
      ))
      waktu = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Waktu(t): "
      ))
      jarak = kecepatan * waktu
      hasil = f"{jarak} m"
      sintephysics(f"Hasil perhitungan Jarak adalah {hasil}")
      loop_feature(physics_bot)

    elif ask_speed == 3:
      kecepatan = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kecepatan(m/s): "
      ))
      jarak = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Jarak(m): "
      ))
      waktu = jarak / kecepatan
      hasil = f"{waktu} s"
      sintephysics(f"Hasil perhitungan Waktu adalah {hasil}")
      loop_feature(physics_bot)

    elif ask_speed == 4:
      sintephysics("Exiting Kecepatan...")
      physics_bot()

  elif ask_choice == 5:
    sintephysics("")
    head_teks("Pilih opsi berikut: ")
    fitur_teks("1. Energi Kinetik(Ek)")
    fitur_teks("2. Energi Potensial(Ep)")
    fitur_teks("3. Exit Energi")

    ask_energi = Prompt.ask(
      "[bold green]Sintesis(Physics): [/bold green]Pilih Opsi: ",
      choices=["1", "2", "3"]
    )

    ask_energi = int(ask_energi)

    if ask_energi == 1:
      massa = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Massa(kg): "
      ))
      kecepatan = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Kecepatan(m/s): "
      ))
      ek = 0.5 * massa * kecepatan ** 2
      hasil = f"{ek} J"
      sintephysics(f"Hasil perhitungan Energi Kinetik adalah {hasil}")
      loop_feature(physics_bot)

    elif ask_energi == 2:
      massa = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Massa(kg): "
      ))
      ketinggian = float(Prompt.ask(
        "[bold green]Sintesis(Physics): [/bold green]Input Ketinggian(m): "
      ))
      ep = massa * 9.8 * ketinggian
      hasil = f"{ep} J"
      sintephysics(f"Hasil perhitungan Energi Potensial adalah {hasil}")
      loop_feature(physics_bot)

    elif ask_energi == 3:
      sintephysics("Exiting Energi...")
      physics_bot()

  elif ask_choice == 6:
    sintephysics("Exiting Physics Mode...")

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
    loop_feature(flight_bot)

  elif ask_menu == 2:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 15000000 
    hasil = f"Harga tiket ke Italy untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    loop_feature(flight_bot)

  elif ask_menu == 3:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 15000000 
    hasil = f"Harga tiket ke France untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    loop_feature(flight_bot)

  elif ask_menu == 4:
    total_in = int(Prompt.ask(
      "[bold green]Sintesis(Flight): [/bold green]ingin berapa orang? "
      ))
    for i in range(total_in):
      harga = i * 5500000 
    hasil = f"Harga tiket ke Singapore untuk {total_in} orang adalah {harga}"
    sinteflight(hasil)
    loop_feature(flight_bot)
  
  elif ask_menu == 5:
    sinteflight("Exiting Flight Mode...")
    physics_bot()
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
def thank_bot():
  hasil = random.choice(bot_dictionary["thank"])
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
    "[bold yellow]Kamu[/bold yellow]"
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
  elif user in dictionary["thank"]:
    thank_bot()
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
