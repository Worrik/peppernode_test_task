# Test task

## To run
Set up env variables (.env-example) and run
```bash
docker compose up -d
docker compose exec django python manage.py migrate
docker compose exec django python manage.py createsuperuser
```
