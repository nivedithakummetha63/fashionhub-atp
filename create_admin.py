import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashionhub.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='KVL@2005').exists():
    User.objects.create_superuser('KVL@2005', 'admin@fashionhub.com', '5002')
    print('Admin KVL@2005 created.')
else:
    print('Admin already exists.')

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin2@fashionhub.com', 'admin')
    print('Admin admin created.')
else:
    print('Admin admin already exists.')
