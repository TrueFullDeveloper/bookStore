# Generated by Django 3.2.3 on 2021-05-31 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210531_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cost',
            field=models.FloatField(default=0, verbose_name='Book Cost'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_count',
            field=models.IntegerField(default=0, verbose_name='Book Count'),
        ),
        migrations.AlterField(
            model_name='deliverycompany',
            name='delivery_cost',
            field=models.FloatField(default=0, verbose_name='Delivery Cost'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.FloatField(default=0, verbose_name='Total Cost'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
    ]