import sqlite3

conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
sql = f'''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            name VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            status_id INTEGER,
            FOREIGN KEY(status_id) REFERENCES Status (id) ON DELETE CASCADE
            );

        CREATE TABLE IF NOT EXISTS Status ( 
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            status VARCHAR(50) NOT NULL
            );

        CREATE TABLE IF NOT EXISTS Product(
                    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                    name VARCHAR(100) UNIQUE NOT NULL,
                    price INTEGER NOT NULL,
                    have BOOLEAN NOT NULL
        
                    );

        CREATE TABLE IF NOT EXISTS SupplyDepartment(
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES User (id) ON DELETE CASCADE,
            FOREIGN KEY(product_id) REFERENCES Product (id) ON DELETE CASCADE
            );

        '''
cursor.executescript(sql)
