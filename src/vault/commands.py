import os
import json
from requests import Request, Session, codes

NO_CONNECTION = "Sem conexão com o servidor"

TOKEN = os.environ.get('TOKEN', None)

KEYS = [
    os.environ.get('KEY1', None),
    os.environ.get('KEY2', None),
    os.environ.get('KEY3', None),
]

class Commands:
    base_url = 'http://' + os.environ.get('BASE_URL', 'vault:8200')

    def create_request(self, request_type, url, data=None, headers=None, content=None):
        url = self.base_url + url
        request_type = request_type.upper()
        s = Session()
        req = Request(
            request_type,
            url,
            data=data,
            headers=headers
        )
        prepare = req.prepare()
        if content:
            prepare.body = content
        resp = s.send(prepare)
        return resp

    def is_on(self):
        # Retorna um booleano correspondente a
        # se a API está inicialidada ou não
        req = self.create_request('get', url='/v1/sys/init')
        if req.status_code == codes.ok:
            return req.json()['initialized']
        raise NO_CONNECTION

    def is_seal(self):
        if self.is_on():
            req = self.create_request('get', url='/v1/sys/seal-status')
            if req.status_code == codes.ok:
                return req.json()['sealed']
        raise NO_CONNECTION

    def unseal(self):
        if self.is_seal:
            for k in KEYS:
                data = { 'key': k }
                req = self.create_request('put', '/v1/sys/unseal', data=json.dumps(data))

    def seal(self):
        header = {'X-Vault-Token': TOKEN}
        req = self.create_request('put', url='/v1/sys/seal', headers=header)

    def create_secret(self, pk, key):
        header = {'X-Vault-Token': TOKEN, 'Content-Type': 'application/json'}
        data = {'key': key}
        req = self.create_request('post', url=f'/v1/secret/user/{pk}', data=json.dumps(data), headers=header)

    def get_secret(self, pk):
        if self.is_seal:
            self.unseal()
            header = {'X-Vault-Token': TOKEN, 'Content-Type': 'application/json'}
            req = self.create_request('get', url=f'/v1/secret/user/{pk}', headers=header)
            if req.status_code == codes.ok:
                return req.json()['data']['key']
            return None


if __name__ == '__main__':
    c = Commands()
    c.unseal()
    print(c.get_secret(2))
    # print(c.is_seal())
    # c.seal()
    # print(c.is_seal())
    # print(KEYS)
    # print(c.is_seal())
    # c.unseal()
    # print(c.is_seal())

