# Generated by Django 3.2.12 on 2022-03-10 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
