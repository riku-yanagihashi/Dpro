from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    icon = models.ImageField(upload_to='icon/', default='icon/default_icon.png', blank=True)
    birthday = models.DateField(blank=True, null=True)

    # Custom related names to avoid conflict
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # 競合回避のために変更
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # 競合回避のために変更
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
