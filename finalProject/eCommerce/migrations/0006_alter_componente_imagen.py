# Generated by Django 3.2.4 on 2021-07-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0005_alter_componente_caracteristica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
