# Generated by Django 3.2.12 on 2022-03-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(db_index=True, default='dsada', max_length=1024),
            preserve_default=False,
        ),
    ]
