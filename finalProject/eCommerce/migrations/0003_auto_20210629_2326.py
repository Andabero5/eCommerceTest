# Generated by Django 3.2.4 on 2021-06-30 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0002_componente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente',
            name='caracteristica',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='componente',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo', to='eCommerce.categoria'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='imagen',
            field=models.CharField(max_length=40),
        ),
    ]
