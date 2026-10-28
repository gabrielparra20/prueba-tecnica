"""Crea o reutiliza una base temporal real desde el servicio demo oficial de Odoo."""
import json
import os
from pathlib import Path
from xmlrpc.client import ServerProxy

CONFIG_PATH = Path('.odoo_demo_local.json')
DEMO_START = 'https://demo.odoo.com/start'


def main():
    if CONFIG_PATH.exists():
        cfg = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
        print('Base de pruebas local recuperada. URL:', cfg['host'])
        print('Base:', cfg['database'])
        return

    print('Solicitando base temporal de demostracion a Odoo...')
    info = ServerProxy(DEMO_START, allow_none=True).start()
    required = {'host', 'database', 'user', 'password'}
    if not isinstance(info, dict) or not required.issubset(info):
        raise RuntimeError('El servicio de demostracion no devolvio los datos requeridos.')

    with os.fdopen(os.open(str(CONFIG_PATH), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'w', encoding='utf-8') as file:
        json.dump({k: info[k] for k in required}, file, indent=2)
    print('Base creada. URL:', info['host'])
    print('Base:', info['database'])
    print('Credenciales guardadas solo en archivo local excluido por .gitignore.')
    print('No comparta, copie al repositorio ni muestre el contenido del archivo.')


if __name__ == '__main__':
    main()



