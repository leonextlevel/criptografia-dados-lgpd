import peewee

# Por hora as credenciais ficarão mockadas para facilitar
HOST = 'drona.db.elephantsql.com'
DATABASE = 'jyzwcidq'
USER = 'jyzwcidq'
PORT = '5432'
PASSWORD = '1UnjUyXHuCRaRsd2jh-A4B1IKSJd3EFK'

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