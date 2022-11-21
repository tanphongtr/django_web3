## Run project

```bash
# Create virtual environment
$ python -m venv virtual_env

# Activate virtual environment
$ source virtual_env/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Export environment variables
$ cp .env.example .env
$ export $(cat .env | xargs)

# Run project
$ python manage.py runserver
```
