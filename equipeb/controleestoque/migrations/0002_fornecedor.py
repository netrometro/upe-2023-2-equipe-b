# Generated by Django 5.0.2 on 2024-02-27 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controleestoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=75)),
                ('sede_local', models.CharField(max_length=150)),
                ('telefone_contato', models.BigIntegerField()),
                ('entrada_data', models.DateTimeField(blank=True, default=datetime.date.today, null=True, verbose_name='Data publicada')),
            ],
        ),
    ]
