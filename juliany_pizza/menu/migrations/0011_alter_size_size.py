# Generated by Django 3.2.12 on 2022-03-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('L', 'L'), ('XL', 'XL'), ('FAMILY', 'FAMILY')], error_messages={'unique': 'That size already exists.'}, max_length=6, unique=True),
        ),
    ]