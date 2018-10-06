import sqlite3 #sqlite is the database used
import os #os is used to delete the database file if necessary
from fake_useragent import UserAgent #provides headers for requests to use
from time import sleep #slow down requests so to prevent ip timeouts. optional

def build():
    '''Build the database if it doesn't exist in the directory.'''
    if os.path.isfile('smiteview.db'):
        conn = sqlite3.connect("smiteview.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE if not exists character
                 (name text, cardloc text, type text, health real, mana real, hp5 real, mp5 text, mvtspd real, range real, physprot real, magprot real, cooldown real, itematkpower real, atkspd real, atkprog text, magpen real, physpen real, crit real, physlifesteal real, maglifesteal real)''')
        conn.commit()
        conn.close()

def update():
    '''Update the database if it exists.'''


def access(operation):
    '''Access the database to either add/delete/update items in it.'''
    if operation == 'help':
        print('Database columns you can view are\nname - god Name\ncardloc - God Image Card Location\ntype - Character Type(Mag or Phys)\nhealth - Health Pool\nmana - Mana Pool\nhp5 - Hp gained over 5 seconds\nmp5 - mp5 gained over 5 seconds\nmvtspd - Movement Speed\nrange - Basic Attack Range\nphysprot - Physical Protection\nmagprot - Magic Protection\ncooldown - Cooldown Percentage\nitematkpower - Item Attack Power\natkspd - Basic Attack Speed\natkprog - Basic Attack Progession\nmagpen - Magical Penetration\nphyspen - Physical Penetration\ncrit - Critical Strike Chance\nphyslifesteal - Physical lifesteal\nmaglifesteal - Magical Lifesteal')

def migrate():
    '''Migrate the database to another database with a different schema'''

def destroy(operation):
    '''Either 'drop' a table or erase a database'''
    if operation == 'drop':
        dropTableStatement = "DROP TABLE if exists character"
        conn = sqlite3.connect("smiteview.db")
        cursor = conn.cursor()
        cursor.execute(dropTableStatement)
        conn.close()
    elif operation == 'erase':
        os.remove('smiteview.db')

def populate():
    '''Populate the character table of the smiteviewer database'''
    ua = UserAgent()
    ua.chrome
    header = {'User-Agent': ua.chrome}
