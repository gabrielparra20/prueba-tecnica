"""Pruebas unitarias SIN depender de la disponibilidad del servicio Odoo."""
import unittest
from importlib.util import module_from_spec, spec_from_file_location

spec = spec_from_file_location('reto_odoo', '02_reto_odoo.py')
reto = module_from_spec(spec)
spec.loader.exec_module(reto)


class ModelosFalsos:
    def __init__(self):
        self.registros = {}
        self.siguiente_id = 100

    def execute_kw(self, db, uid, password, modelo, metodo, args, opciones=None):
        assert modelo == 'res.partner'
        assert db == 'demo_test' and uid == 7 and password == 'clave_ficticia'
        if metodo == 'search_read':
            dominio = args[0]
            referencia = next(valor for campo, operador, valor in dominio if campo == 'ref' and operador == '=')
            encontrados = [dict(r) for r in self.registros.values() if r.get('ref') == referencia]
            return encontrados[:(opciones or {}).get('limit', 80)]
        if metodo == 'create':
            valores = dict(args[0])
            registro_id = self.siguiente_id
            self.siguiente_id += 1
            self.registros[registro_id] = {'id': registro_id, **valores}
            return registro_id
        if metodo == 'write':
            ids, valores = args
            for registro_id in ids:
                self.registros[registro_id].update(valores)
            return True
        raise AssertionError(f'Metodo inesperado: {metodo}')


class PruebaJunior(unittest.TestCase):
    def test_telefono_10_digitos(self):
        self.assertEqual(reto.normalizar_telefono('300 123 4567'), '3001234567')
        self.assertEqual(reto.normalizar_telefono('(311) 222-3344'), '3112223344')

    def test_telefono_invalido(self):
        with self.assertRaises(ValueError):
            reto.normalizar_telefono('123')

    def test_crear_y_actualizar_sin_duplicar(self):
        modelos = ModelosFalsos()
        info = {'database': 'demo_test', 'password': 'clave_ficticia'}
        primero = reto.guardar_contacto(modelos, info, 7, 'WT-JUNIOR-X9', 'Inicial', '3001234567')
        segundo = reto.guardar_contacto(modelos, info, 7, 'WT-JUNIOR-X9', 'Actualizado', '3112223344')
        self.assertEqual(primero, segundo)
        self.assertEqual(len(modelos.registros), 1)
        self.assertEqual(modelos.registros[primero]['phone'], '3112223344')
        self.assertEqual(modelos.registros[primero]['name'], 'Actualizado')


if __name__ == '__main__':
    unittest.main()
