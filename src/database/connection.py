import os
import peewee

# Por hora as credenciais ficarão mockadas para facilitar
HOST = 'db'
DATABASE = os.environ.get('DB_DATABASE')
USER = os.environ.get('DB_USER')
PORT = '5432'
PASSWORD = os.environ.get('DB_PASSWORD')

DATABASE_URL = f'postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

db = peewee.PostgresqlDatabase(
    DATABASE,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

if __name__ == '__main__':
    import pdb; pdb.set_trace()
    print(DATABASE_URL)