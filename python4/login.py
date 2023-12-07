from status import STATUS,UserExecutor
from db import cursor,conn


def authorization():
    username = input('Имя: ')
    password = input('Пароль: ')
    user = cursor.execute("SELECT * FROM User JOIN Status ON User.status_id = Status.id WHERE User.name = ? AND User.password = ?",(username,password)).fetchone()
    id,status = user['id'],user['status']
    return STATUS[status](id)

def signup():
    username = input('Придумайте имя: ')
    password = input('Придумайте пароль: ')
    UserExecutor.insert({'name':username,'password':password,'status_id':1})
    return STATUS['buyer'](cursor.lastrowid)