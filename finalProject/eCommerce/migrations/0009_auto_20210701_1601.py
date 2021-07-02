# Generated by Django 3.2.4 on 2021-07-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0008_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='componente',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
