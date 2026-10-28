# WONDERTECH | Reto Odoo + Python + Git + IA (30 minutos)

## Preparación ANTES del tiempo evaluado

- Computador, internet, Python 3.10+, Git, editor VS Code y navegador.
- Iniciar sesión en la cuenta PERSONAL de GitHub y tener Git configurado.
- Abrir Codex o Claude Code; si el acceso a alguna herramienta es limitado,
  acordar antes con el evaluador una alternativa de IA generativa disponible.
- No es necesario instalar Odoo ni pagar una licencia. No usar cuentas de Wondertech.
- Microsoft Teams: compartir pantalla durante los 30 minutos.

## Desarrollo DURANTE los 30 minutos

1. Abra una terminal en la carpeta de estos archivos.
2. Ejecute `python 01_crear_base.py`. Genera una base temporal real y guarda
   credenciales SOLO en `.odoo_demo_local.json` (ignorado por Git).
3. Ejecute `python -m unittest -v test_local.py`. Los fallos iniciales son parte del reto.
4. Corrija los DOS errores intencionales de `02_reto_odoo.py`.
5. Complete `guardar_contacto` mediante `models.execute_kw` / API XML-RPC.
   Debe crear un contacto en `res.partner`, actualizarlo y evitar duplicados.
6. Repita las pruebas locales hasta que pasen.
7. Ejecute `python 02_reto_odoo.py CAND-01` (cambie el alias asignado).
   Debe imprimir `OK - ODOO MODIFICADO POR API` con ID y referencia.
8. Use su propia cuenta GitHub; haga commit y push a un repositorio PRIVADO.
   Otorgue acceso al evaluador designado o muestre en vivo el enlace y commit.
9. Explique en 2 minutos que corrigio, que hizo la IA y por que su solucion
   no crea duplicados. Nunca copie secretos en herramientas de IA.

## Entregables

- Demostración en vivo: base temporal y registro en Odoo creado/actualizado.
- Resultado `python -m unittest -v test_local.py` (3 tests OK).
- Repositorio privado en cuenta GitHub del candidato; al menos un commit.
- Explicacion oral; no requiere documento adicional.

## Ejemplo de comandos Git (si ya configuro GitHub)

    git init
    git add 01_crear_base.py 02_reto_odoo.py test_local.py .gitignore README_INICIO.md
    git commit -m "Reto Wondertech: integracion Odoo"
    git branch -M main
    git remote add origin URL_PRIVADA_DEL_REPOSITORIO
    git push -u origin main

El enlace y el acceso se gestionan con el evaluador. No pegue credenciales en el chat.
Si falla el servicio de bases demo por una causa externa, informe de inmediato:
la empresa debe activar la contingencia; no es un error atribuible al candidato.

Al terminar, borre `.odoo_demo_local.json` y cualquier secreto temporal.

Referencia: Odoo 19 - External RPC API > Test database
https://www.odoo.com/documentation/19.0/developer/reference/external_rpc_api.html
