# Generated by Django 4.0.1 on 2022-09-15 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0007_alter_ingrediants_options_alter_menuitems_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaselog',
            old_name='date',
            new_name='timestamp',
        ),
    ]
