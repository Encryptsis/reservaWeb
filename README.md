# Reserva Web

Proyecto Django para gestionar reservas de restaurante con una landing pública y un backend inicial sobre SQLite.

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

## Qué incluye el backend actual

- Formulario público conectado a Django para guardar reservas.
- Modelo `Reservation` con nombre, email, teléfono, fecha, hora, comensales y peticiones especiales.
- Estado inicial de la reserva (`pending`, `confirmed`, `cancelled`).
- Gestión de reservas desde el panel de administración en `/admin/`.

## Desarrollo sin Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
