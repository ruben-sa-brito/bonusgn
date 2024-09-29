# Generated by Django 5.1.1 on 2024-09-28 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_name', models.CharField(default='Bonus', max_length=40, verbose_name='Defina um nome para esta bonificação')),
                ('active_ranges', models.BooleanField(default=False, verbose_name='Marque para ativar esta bonificação')),
                ('active_percentage', models.BooleanField(default=False, verbose_name='Definir última faixa como porcentagem')),
            ],
        ),
        migrations.CreateModel(
            name='SaleRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_range', models.CharField(max_length=40, verbose_name='Faixas')),
                ('value', models.FloatField()),
                ('sales_ranges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bonus.salesranges')),
            ],
        ),
    ]
