# Generated by Django 5.1.1 on 2024-09-18 16:12

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_user_is_superuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VTD',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('value', models.IntegerField(verbose_name='amount')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 9, 19, 1, 12, 47, 375797))),
            ],
        ),
        migrations.CreateModel(
            name='VTDlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='amount')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2024, 9, 19, 1, 12, 47, 375797))),
                ('vtd_from', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vtd_from', to=settings.AUTH_USER_MODEL)),
                ('vtd_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vtd_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]