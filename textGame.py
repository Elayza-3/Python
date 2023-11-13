import random
import json
import csv
import os

# Инициализация переменных
TREASURES = {
    'монета',
    'золотая руда',
    'рубин',
    'волшебный кулон',
    'плащ невидимка',
    'клинок',
    'ожерелье',
    'магическая руна'
}

class Character:
    def __init__(self,health=100,items={},gold=0,kill=0,step=1):
        self.health = health
        self.items = items.copy()
        self.gold = gold
        self.kill = kill
        self.step=step

    def update_thing(self,name):
        self.items[name] = self.items.get(name, 0) + 1

    def get_info(self):
        return [
            self.health,
            self.items,
            self.gold,
            self.kill,
            self.step,
        ]

class Location:
    MEET_MONSTER=(False,False,True,False)

    def __init__(self,name,treasures):
        self.name = name
        self.treasures: set = treasures

    def get_monster(self):
        if random.choice(self.MEET_MONSTER):
            battle()

    def get_treasure(self):
        lst = list(self.treasures)+['']
        random.shuffle(lst)

        treasure = random.choice(lst)
        # print(lst,treasure)
        self.get_monster()
        if treasure:
            print(f"Вы нашли сокровище - {treasure}")
            character.update_thing(treasure)
        else:
            print("Сокровищ нет(")
        print("________________")
        print("Ваш текущий арсенал:")
        for key,item in character.items.items():
            print(f"{key} - {item}")
        print("________________")

    def get_description(self):
        description = f"""
                        Вы попали в локацию \"{self.name.capitalize()}\"
                        В этой локации можно найти сокровища: {list(self.treasures)}
                       """
        print(description)


def save_changes():
    save = input('Сохранить изменения?(да/нет)')
    if save == 'да':
        if saves.get(player_name, False):
            change = input('У вас уже есть сохранение! Перезаписать?')
            if change == 'да':
                saves[player_name] = character.get_info()
        saves.setdefault(player_name, character.get_info())
        with open('saves.json', 'w', encoding='utf-8') as jsfile:
            with open('saves.csv', 'a+', encoding='utf-8') as csv_file:
                csv.writer(csv_file).writerow(character.get_info())
            json.dump(saves, jsfile, indent=4, ensure_ascii=False)


locations = {

    Location("темный лес",{
        'плащ невидимка',
        'клинок',}
             ),

    Location("хижина",{
        'рубин',
        'клинок',}
             ),

    Location("мистическая долина",{
        'рубин',
        'ожерелье',}
             ),

    Location("шахта",{
        'монета',
        'золотая руда',}
             ),
    Location("затерянный край",{
        'магическая руна',
        'волшебный кулон',}
             )
}
# Приветствие
print("Добро пожаловать в текстовую игру!")

try:
    with open('saves.json', 'r', encoding='utf-8') as file:
        data = file.read()

        if not data:
            data = '{}'

        saves = json.loads(data)
except:
    with open('saves.json', 'w', encoding='utf-8') as file:pass
    saves={}

# Выбор имени игрока
player_name = input("Как тебя зовут? ")
if saves.get(player_name, False):
    answer = input('У вас есть сохранение, загрузить?(да/нет)')
    if answer == 'да':
        character = Character(*saves.get(player_name))
        direction = input("Куда теперь? (вперед/налево/направо)")


else:
    # Вступление в игру
    print(f"Привет, {player_name}! Ты оказался в загадочном мире, где тебя ждут увлекательные приключения.")
    print(f"{len(TREASURES)} волшебных предметов были растеряны на разных локациях")
    print("Ваша задача их отыскать, но в во время поиска на вас может напасть монстр!")
    print("У вас будет выбор атаковать или защищаться (тем самым получив меньше урона)")
    print(
        "Но также если вы соберете два волщебных предмета: клинок и плащ невидимка - то вам будут доступны новые действия")

    # Начало игры
    print("Ты стоишь на перекрестке дорог. Куда ты хочешь пойти? (вперед/налево/направо)")
    direction = input().lower()
    character = Character()

# Функция для боя с монстром
def battle():

    monster_health = random.randint(30, 50)
    print(f"Ты встретил монстра с {monster_health} здоровья!")
    actions = "атаковать/защищаться"

    if character.items.get("клинок",0):
        actions += "/мгновенное убийство"
    if character.items.get("плащ невидимка",0):
        actions += "/скрыться"

    while character.health > 0 and monster_health > 0:

        action = input(f"Что ты хочешь сделать? ({actions}): ")
        if action == "атаковать":
            damage = random.randint(10, 20)
            print(f"Ты нанес {damage} урона монстру!")
            monster_health -= damage
            if monster_health > 0:
                print(f"Монстр атакует тебя и наносит {random.randint(5, 15)} урона!")
                character.health -= random.randint(5, 15)
        elif action == "защищаться":
            print("Ты защищаешься и получаешь меньше урона от монстра.")
            character.health -= random.randint(5, 10)
            if monster_health > 0:
                print(f"Монстр атакует тебя и наносит {random.randint(5, 15)} урона!")
                character.health -= random.randint(5, 15)
        elif action == "мгновенное убийство" and character.items["клинок"]!=0:
            character.items["клинок"]-=1
            monster_health=0
        elif action == "скрыться" and character.items["плащ невидимка"]!=0:
            character.items["плащ невидимка"]-=1
            print("Вы сумели скрыться")
            return
        else:
            print("Неверное действие! Попробуй еще раз.")
    if character.health <= 0:
        print("Ты проиграл! Игра окончена.")
    else:
        print("Ты победил монстра и получаешь 50 золотых!")
        character.gold += 50
        character.kill+=1

def ask(location):
    location.get_description()
    choice = input("Ты хочешь взять сокровище?(да/нет): ")
    if choice == "да":
        location.get_treasure()
    else:
        print("Ты решил не брать сокровищ и продолжил свой путь.")

# Основной игровой цикл
while True:
    location = random.choice(list(locations))
    if direction == "вперед":
        print("Ты свернул вперед")
        location.get_description()
        choice = input("Ты хочешь взять сокровище?(да/нет): ")
        if choice == "да":
            location.get_treasure()
        else:
            print("Ты решил не брать сокровищ и продолжил свой путь.")
    elif direction == "налево":
        print("Ты свернул налево")
        location.get_description()
        choice = input("Ты хочешь взять сокровище?(да/нет): ")
        if choice == "да":
            location.get_treasure()
        else:
            print("Ты решил не брать сокровищ и продолжил свой путь.")
    elif direction == "направо":
        print("Ты свернул направо")
        location.get_description()
        choice = input("Ты хочешь взять сокровище?(да/нет): ")
        if choice == "да":
            location.get_treasure()
        else:
            print("Ты решил не брать сокровищ и продолжил свой путь.")
    elif direction=="save":
        save_changes()
    else:
        print("Неверное направление! Попробуй еще раз.")

    if len(character.items) == len(TREASURES):
        print("Победа!!!! Вы собрали все предметы")
        break
    elif character.step>=100:
        print("Слишком много ходов")
        break

    # Проверка состояния здоровья
    if character.health <= 0:
        print("Ты проиграл! Игра окончена.")
        break

    # Выбор следующего направления
    direction = input("Куда теперь? (вперед/налево/направо)")
    character.step+=1

# Завершение игры
print(f"Спасибо за игру, {player_name}! До новых приключений!")
print("Ваш результат:")
print("____________")
print(f"Убито монстров - {character.kill}")
print(f"Собрано золота - {character.gold}")
print(f"Колличество шагов - {character.step}")
print(f"Всего собрано предметов - {sum(character.items.values())}")
print("____________")



