# Generated by Django 2.0.4 on 2021-04-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210405_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreMarketStocks',
            fields=[
                ('stock_ticker', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=200)),
                ('last_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('grow_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('grow_price_sinal', models.CharField(max_length=1, null=True)),
                ('grow_percentage', models.DecimalField(decimal_places=4, max_digits=10)),
                ('active', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'PreMarketStocks',
                'db_table': 'PreMarketStocks',
            },
        ),
    ]