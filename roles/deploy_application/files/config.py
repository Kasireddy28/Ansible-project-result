import os

SECRET_KEY = os.getenv('SECRET_KEY', 'default_key')
DB_PATH = os.getenv('DB_PATH', 'sqlite:///default.db')
ADMIN_GROUPS = os.getenv('ADMIN_GROUPS', 'Read-only')
