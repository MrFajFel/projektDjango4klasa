# Generated by Django 4.2.17 on 2025-01-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0010_alter_user_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
