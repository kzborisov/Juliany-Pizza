# Generated by Django 3.2.12 on 2022-03-18 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0020_rename_menuitem_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]