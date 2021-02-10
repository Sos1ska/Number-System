import os
Green = '\033[92m'
Red = '\033[91m'
Default = '\033[99m'
end       = '\033[0m'
Yellow = '\033[93m'
input(f"{Default}Начать Установку доп. компонентов? {end}{Green}Y{end}{Default}/{end}{Red}N{end}")
is_install = (Green + ">>> " + end)

if str(is_install) == "Y" "y":
    print("Начинаю установку")
    mod = ("figlet", "toillet", "cowsay", "nano", "rudy")
    for i in range(len(mod[i])):
        os.system("pkg install "+mod[i]+"-y")
        os.system("clear")
        
os.system("gem install lolcat")
print(f"{Yellow}Установка завершена, введите python3 Breaking.py для запуска{end}")