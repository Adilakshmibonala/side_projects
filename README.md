# MultiPair VideoChat WebApplication Using DjangoWebSocket and WebRTC


## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
```

## install requirements

```bash
pip install -r requirements.txt
```

## running django management commands & usage

```sh
export DJANGO_SETTINGS_MODULE=fastor.settings
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```