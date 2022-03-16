# Generated by Django 3.2.12 on 2022-03-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_size_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('L', 'L'), ('XL', 'XL'), ('FAMILY', 'FAMILY')], error_messages={'unique': 'That size already exists.'}, max_length=7, unique=True),
        ),
    ]