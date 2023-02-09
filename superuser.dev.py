import os

import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

User = get_user_model()

try:
    admin = User.objects.get(email="admin@admin.com")

    if not admin.check_password("123456"):
        admin.set_password("123456")
        admin.save()

except User.DoesNotExist:
    User.objects.create_superuser(
        username="admin", email="admin@admin.com", password="123456"
    )

print("Created Django Username: admin and Password: 123456.")
