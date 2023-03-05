import sqlite3 as sq

def import_img_binary(img_path):
    # Преобразование данных в двоичный формат
    f = open(img_path, 'rb')
    img_binary = f.read()
    return img_binary

def sql_start():
    global base, cur
    base = sq.connect("photo_editor.db")
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img BLOB, blur TEXT, color TEXT)')
    
    base.commit()
    
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()