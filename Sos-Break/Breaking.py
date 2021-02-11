import urllib.request
import json
import os

# Цвета
Red = '\033[91m'
Green = '\033[92m'
Blue = '\033[94m'
Cyan = '\033[96m'
White = '\033[97m'
Yellow = '\033[93m'
Magenta = '\033[95m'
Grey = '\033[90m'
Black = '\033[90m'
Default = '\033[99m'
Underline = '\033[4m'
end       = '\033[0m'

print(f"{Red}\t\t{Underline}Sos1ska-Breaking 1.0{end}")

os.system("toilet -f big ' Sos1ska-Hackers' -F gay | lolcat")

print()
print(f"{Default}Код написан{end}", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Red}Sos1ska-Hackers{end}")
print()

print()
print(f"{Default}ВКонтакте", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Default}https://vk.com/nikitasos1ska  {end}", end="")
print(f"{Default}  Почта", end="")
print(f"{Green} >>> {end}", end="")
print(f"{Default}soshack00@gmail.com{end}", end="")
print()

# Установка номера телефона для пробива
print(f"{Red}{Underline}Внимание, номер должен содержать +7{end}")
print(f"{Default}Введите номер телефона для пробива{end}")
number = input(Green + ">>> " + end)

# Установка информации
getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + number
try:
        infoNumber = urllib.request.urlopen( getInfo )

except:
        print(f"\n[!] - {Red}Номер введён не верно{end} - [!]\n")

infoNumber = json.load( infoNumber )

print(f"{Blue}Страна {end}{Green}>>> {end}", infoNumber["country"]["fullname"])
print(f"{Blue}Столица {end}{Green}>>> {end}", infoNumber["capital"]["name"])
print(f"{Yellow}Широта столицы {end}{Green}>>> {end}", infoNumber["capital"]["latitude"])
print(f"{Yellow}Долгота столицы {end}{Green}>>> {end}", infoNumber["capital"]["longitude"])
print(f"{Yellow}Тип времени {end}{Green}>>> {end}+", infoNumber["capital"]["time_zone"])
print(f"{Magenta}Код номера {end}{Green}>>> {end}", infoNumber["country"]["country_code3"])
print(f"{Magenta}MCC номера {end}{Green}>>> {end}", infoNumber["country"]["mcc"])
print(f"{Magenta}Регион {end}{Green}>>> {end}", infoNumber["region"]["name"])
print(f"{Yellow}Округ {end}{Green}>>> {end}", infoNumber["region"]["okrug"])
print(f"{Yellow}Код региона {end}{Green}>>> {end}", infoNumber["region"]["autocod"])
print(f"{Yellow}Город {end}{Green}>>> {end}", infoNumber["0"]["name"])
print(f"{Magenta}Широта города {end}{Green}>>> {end}", infoNumber["0"]["latitude"])
print(f"{Magenta}Долгота города {end}{Green}>>> {end}", infoNumber["0"]["longitude"])
print(f"{Magenta}Oper_id {end}{Green}>>> {end}", infoNumber["0"]["oper_id"])
print(f"{Yellow}Радиус номеров телефонов {end}{Green}>>> {end}", infoNumber["0"]["def"])
print(f"{Yellow}Рабочесть телефона {end}{Green}>>> {end}", infoNumber["0"]["mobile"])
print(f"{Yellow}Оператор {end}{Green}>>> {end}", infoNumber["0"]["oper"])
