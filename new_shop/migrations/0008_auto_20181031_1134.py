# Generated by Django 2.1.2 on 2018-10-31 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_shop', '0007_auto_20181023_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=300, verbose_name='адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zacaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(1, 'В обработке'), (2, 'Доставка'), (3, 'Готово')], max_length=10, verbose_name='статус заказа')),
                ('items', models.ManyToManyField(blank=True, to='new_shop.CardItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='item',
            field=models.ManyToManyField(blank=True, to='new_shop.CardItem'),
        ),
    ]