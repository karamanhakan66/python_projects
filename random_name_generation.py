import random
def generate_random_name():
    first_names =["Alex","Mustafa","Mahmut","Ali","Mehmet","Ayşe","Fatma","Emine","Zeynep","Elif","Hakan"]
    last_names = ["Yılmaz","Bekdemir","Karaman","De Souza","Kara","Demir","Çelik","Koç","Aydın","Öztürk"]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f"{first_name} {last_name}"

    
print(generate_random_name())