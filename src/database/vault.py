import os
import asyncio

import async_hvac


client = async_hvac.AsyncClient(url='http://localhost:8200', token=os.environ['VAULT_TOKEN'])

async def get_secrets():

    await client.write('secret/tests', fruta='abacate')

    secrets = await client.read('secret/tests')

    await client.close()
    
    print(secrets)


asyncio.run(get_secrets())

client = hvac.Client(url='http://localhost:8200')



client.secrets.kv.v2.create_secret(
    path='foo',
    secret={'5': 'ashadjad'},
)