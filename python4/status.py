from db import cursor
from executor import *


class NamePasswordChange:
    def __init__(self,id):
        self.id = id

    def set_new_profile(self):
        new_name = input('Введите новое имя: ')
        new_password = input('Введите новый пароль: ')
        UserExecutor.update({'name':new_name,'password':new_password},{'id':self.id})
        print('Изменения сохранены')


def receive_values(dictionary):
    keys = dictionary.keys()
    values = []
    for key in keys:
        values.append(dictionary[key])
    return values

def exceptions(func):
    def inner(*args,**kwargs):
        while True:
            try:
                print('КОМАНДЫ:')
                print('_'*30)
                res = func(*args,**kwargs)

                if res == '':
                    return
                elif res is None:
                    print('Операция выполнена')
                elif not res is None:
                    print('Такого действия нет')
            except ValueError as ve:
                print(ve)
            except:
                print('Произошла ошибка(')
            print('_' * 30 + '\n')
    return inner

def print_list(lst):
    for record in lst:
        print(*receive_values(record),sep='  |  ')

class Buyer(NamePasswordChange):

    def record_product(self):
        name = input('Введите название продукта: ')
        product = ProductExecutor.get({'name':name})
        SupplyDepartmentExecutor.insert({'user_id':self.id,'product_id':product['id']})
        print('Заказ оформлен')

    @staticmethod
    def remove_product():
        name = input('Введите название продукта: ')
        product = cursor.execute('SELECT * FROM SupplyDepartment JOIN Product ON SupplyDepartment.product_id = Product.id WHERE name = ?', (name,)).fetchone()
        SupplyDepartmentExecutor.raise_is_none(product)
        SupplyDepartmentExecutor.delete({'product_id':product['id']})
        print('Продукт удален')

    @exceptions
    def commands(self):
        print('1. Заказать продукт')
        print('2. Отменить заказ продукта')
        print('3. Показать все продукты')
        print('4. Показать продукты (в наличие)')
        print('5. Изменить профиль')


        command = input()
        if command == '1':
            self.record_product()
        elif command == '2':
            self.remove_product()
        elif command == '3':
            print_list(ProductExecutor.getAll())
        elif command == '4':
            print_list(ProductExecutor.filter({'have': True}))
        elif command == '5':
            self.set_new_profile()
        else : return command


class Admin(NamePasswordChange):

    @exceptions
    def commands(self):
        print('1. Добавить продукт')
        print('2. Удалить продукт')
        print('3. Показать все продукты')
        print('4. Показать продукты (в наличие)')
        print('5. Фильтрация')
        print('6. Изменить профиль')

        command = input()
        if command == '1':
            ProductExecutor.insert(ProductExecutor.create())
        elif command == '2':
            ProductExecutor.delete({'name': input('Название продукта: ')})
        elif command == '3':
            print_list(ProductExecutor.getAll())
        elif command == '4':
            print_list(ProductExecutor.filter({'have': True}))
        elif command == '5':
            print_list(ProductExecutor.filter(ProductExecutor.create()))
        elif command == '6':
            self.set_new_profile()
        else: return command

class SuperUser(NamePasswordChange):

    @exceptions
    def commands(self):
        print('1. Добавить пользователя')
        print('2. Удалить пользователя')
        print('3. Показать всех пользователей')
        print('4. Фильтрация')
        print('5. Изменить профиль')
        print('6. Роли')

        command = input()
        if command == '1':
            UserExecutor.insert(UserExecutor.create())
        elif command == '2':
            UserExecutor.delete({'name': input('Имя пользователы: ')})
        elif command == '3':
            print_list(UserExecutor.getAll())
        elif command == '4':
            print_list(UserExecutor.filter(UserExecutor.create()))
        elif command == '5':
            self.set_new_profile()
        elif command == '6':
            print_list(StatusExecutor.getAll())
        else: return command


STATUS = {
    'buyer':Buyer,
    'admin':Admin,
    'superuser':SuperUser
}
