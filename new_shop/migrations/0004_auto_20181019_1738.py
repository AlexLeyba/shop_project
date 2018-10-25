# Generated by Django 2.1.2 on 2018-10-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_shop', '0003_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='text',
            new_name='rodcat',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sail',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Скидка'),
        ),
    ]
