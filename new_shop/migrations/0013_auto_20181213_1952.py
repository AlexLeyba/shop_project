# Generated by Django 2.1.2 on 2018-12-13 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_shop', '0012_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_one', models.IntegerField(default=0, verbose_name='1 звезда')),
                ('star_two', models.IntegerField(default=0, verbose_name='2 зыезды')),
                ('star_three', models.IntegerField(default=0, verbose_name='3 зыезды')),
                ('star_four', models.IntegerField(default=0, verbose_name='4 зыезды')),
                ('star_five', models.IntegerField(default=0, verbose_name='5 зыезд')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new_shop.Rating'),
            preserve_default=False,
        ),
    ]
