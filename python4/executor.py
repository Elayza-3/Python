import sqlite3
from db import cursor,conn

class Executor:

    def __init__(self,name_table):
        self.conn = conn
        self.cursor = cursor
        self.name_table = name_table

    def executeQuery(self,query,data = tuple()):

        try:
            # print(query,tuple(data))
            result = self.cursor.execute(query,tuple(data))
            if data:
                conn.commit()
            return result.fetchall()
        except sqlite3.Error as ex:
            print('Ошибка',ex)
            raise ex

    def raise_is_none(self,value,msg = 'Позиция(-ии) не найдена(-ы)'):
        if value is None or not value :
            raise ValueError(msg)
        return value

    def filter(self,cond):
        result = self.executeQuery(f"SELECT * FROM {self.name_table} WHERE {self._get_cond(cond)}",cond.values())
        return self.raise_is_none(result)

    def get(self,cond):
        return self.filter(cond)[0]

    def _get_cond(self,cond):
        return ' AND '.join([f'{column} = ?' for column in cond.keys()])

    def getAll(self):
        return self.executeQuery(f"SELECT * FROM {self.name_table}")

    def delete(self,cond):
        return self.executeQuery(f"DELETE FROM {self.name_table} WHERE {self._get_cond(cond)}",cond.values())

    def update(self,fields,cond):#PRAGMA table_info("user")
        return self.executeQuery(f"UPDATE {self.name_table} SET {'=?,'.join(fields.keys())} WHERE {self._get_cond(cond)}",tuple(*fields.values(),*cond.values()))

    def insert(self,fields):
        return self.executeQuery(f"INSERT INTO {self.name_table}({','.join(fields.keys())}) VALUES({','.join(['?']*len(fields))})",fields.values())

class ProductExecutorClass(Executor):
    def create(self):
        new_product = {
            'name': input('Название продукта: '),
            'price': abs(int(input('Цена: '))),
            'have': bool(int(input('Наличие (1/0): '))),

        }
        return new_product

class UserExecutorClass(Executor):
    def create(self):
        new_user = {
            'name': input('Имя: : '),
            'password': input('Пароль: '),
            'status_id': int(input('Роль: ')),

        }
        return new_user

UserExecutor = UserExecutorClass('User')
StatusExecutor = Executor('Status')
SupplyDepartmentExecutor = Executor('SupplyDepartment')
ProductExecutor = ProductExecutorClass('Product')

