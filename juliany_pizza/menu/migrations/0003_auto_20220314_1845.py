# Generated by Django 3.2.12 on 2022-03-14 18:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(choices=[('Tomatoes', 'Tomatoes'), ('Cheese', 'Cheese')], max_length=8),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
                ('ingredients', models.ManyToManyField(to='menu.Ingredient')),
            ],
            options={
                'verbose_name': 'Menu Items',
                'verbose_name_plural': 'Menu Item',
            },
        ),
    ]