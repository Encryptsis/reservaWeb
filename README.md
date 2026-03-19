# Reserva Web

Base inicial de Django preparada para ejecutarse con Docker.

## Requisitos

- Docker
- Docker Compose

## Puesta en marcha

1. Copia las variables de entorno:

   ```bash
   cp .env.example .env
   ```

2. Construye e inicia el contenedor:

   ```bash
   docker compose up --build
   ```

3. Abre `http://localhost:8000`.

## Desarrollo sin Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
