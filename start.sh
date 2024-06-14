#!/bin/sh

# Esperar 5 segundos antes de intentar iniciar la aplicación
sleep 5

# Iniciar la aplicación Flask
exec python3 -m flask --app main.py --debug run --host=0.0.0.0