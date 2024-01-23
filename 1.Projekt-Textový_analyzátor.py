"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Rastislav Uhrin
email: uhrin.rasto@gmail.com
discord: Rasťo U#4790
"""

"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+
"""
# import textov a pomocné premenné
import task_template
text_vyber = ("1","2","3")
prac_text = list()          # rozdelený text na slová a čísla, upravený o .,:;
cisla_z_textu = list()      # vyčlenené čísla z textu
slova_z_textu = list()      # vyčlenené slová (string) z textu
dlzka_slova = dict()        # pomocný slovník na dĺžku jednotlivých slov (počet písmen)
pocet_slov = 0              # celkový počet slov
pocet_cisel = 0             # celkový počet čísel
prve_velke = 0              # počet slov, začínajúcich veľkým písmenom
vsetky_velke = 0            # počet slov, napísaných veľkými písmenami
vsetky_male = 0             # počet slov, napísaných malými písmenami
cisla = list()              # zoznam čísel pre výpočet ich súčtu
cara = "-" * 70             # pomocná oddeľujúca čiara

# užívatelia a ich heslá
users = {'bob' : '123', 'ann' : 'pass123', 
        'mike' : 'password123', 'liz' : 'pass123'}

# prihlásenie užívateľa
username = input("username:")       
if username not in users:
    print(f"{cara}\nunregistered user, terminating the program \n{cara}")
    quit()
else:
    # zadanie hesla
    password = input("password:")   

if password != users[username]:
    print(f"{cara}\nwrong password, terminating the program \n{cara}")    
    quit()
else: 
    # uvítanie a výber textu k analyzovaniu   
    print(f"{cara}\nWelcome to the app, {username}")
    print(f"We have 3 texts to be analyzed.\n{cara}")
    text_no = (input("Enter a number btw. 1 and 3 to select: "))

    # kontrola či je text v zozname
if text_no not in text_vyber:
    print(f"{cara}\nyou entered value different from  1 - 3, terminating the program \n{cara}")    
    quit()            
else:        
    # príprava textu pre ďalšie kroky
    pom_text = (task_template.TEXTS[int(text_no)-1]).split(" ")
            
    # výpočet počtu slov a čísel v texte podľa zadania
    for slovo in pom_text:
                prac_text.append(slovo.strip(",.:;"))
                pocet_slov +=1
                if slovo.isnumeric():
                   pocet_cisel += 1
                   cisla.append(int(slovo))
                elif slovo.islower():
                     vsetky_male += 1    
                elif slovo.isupper() and slovo.isalpha():
                     vsetky_velke += 1
                elif slovo[0].isupper():
                     prve_velke += 1          
                
              
    # výstupy počtov slov, čísel
    print(f"""{cara}
There are {pocet_slov} words in the selected text.
There are {prve_velke + vsetky_velke} titlecase words.
There are {vsetky_velke} uppercase words.
There are {vsetky_male} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers {sum(cisla)}
{cara}
LEN\t|  OCCURENCES  \t\t|NR.
{cara}""")           
            
    # príprava na počet písmen jednotlivých slov a koľko takých slov je
    for slovo_2 in prac_text:
        slovo_3 = len(slovo_2)
        if slovo_3 not in dlzka_slova:
           dlzka_slova[slovo_3] = 1
        else:
           
           dlzka_slova[slovo_3] += 1
            
    # zoradenie slovníka od najkratšieho po najdlhšie slovo            
    dlzka_slova_pom = list(dlzka_slova.keys())         # z dict som vytvoril list kvôli zoradeniu podľa keys
    dlzka_slova_pom.sort()
    sorted_dlzka = {i: dlzka_slova[i] for i in dlzka_slova_pom} 

    # príprava na výstup vo forme "grafu" z hviezdičiek
    for x,y in sorted_dlzka.items():
        hviezdicky = y * "*"
        if len(hviezdicky) > 14:
           print(f"{x}\t|{hviezdicky}\t| {y}")
        elif len(hviezdicky) > 6:
             print(f"{x}\t|{hviezdicky}\t\t| {y}")
        else:
             print(f"{x}\t|{hviezdicky}\t\t\t| {y}")
