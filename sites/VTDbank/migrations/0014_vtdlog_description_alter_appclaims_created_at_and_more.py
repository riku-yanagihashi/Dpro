# Generated by Django 5.1.1 on 2024-09-26 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VTDbank', '0013_alter_claims_created_at_alter_messages_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vtdlog',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='appclaims',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 19, 57, 49, 720987)),
        ),
        migrations.AlterField(
            model_name='claims',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 19, 57, 49, 720987)),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 19, 57, 49, 720987)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 19, 57, 49, 720987)),
        ),
        migrations.AlterField(
            model_name='vtdlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 19, 57, 49, 719985)),
        ),
    ]
