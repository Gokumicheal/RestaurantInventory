# Generated by Django 4.1.1 on 2022-09-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_purchaselog_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediants',
            name='price_per_unit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingrediants',
            name='unit',
            field=models.CharField(choices=[('kg', 'KG'), ('gm', 'Gram'), ('lr', 'Litre'), ('ou', 'Ounces')], max_length=2),
        ),
        migrations.AlterField(
            model_name='menuitems',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='purchaselog',
            name='quantity',
            field=models.FloatField(default=1),
        ),
    ]
