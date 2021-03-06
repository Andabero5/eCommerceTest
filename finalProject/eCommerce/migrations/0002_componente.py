# Generated by Django 3.2.4 on 2021-06-30 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.CharField(max_length=30)),
                ('caracteristica', models.CharField(max_length=150)),
                ('precio', models.CharField(max_length=7)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eCommerce.categoria')),
            ],
        ),
    ]
