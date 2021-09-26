# Generated by Django 3.2.6 on 2021-09-25 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='название')),
                ('city', models.CharField(max_length=32, verbose_name='название города')),
                ('phone', models.CharField(max_length=20, verbose_name='номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email адресс')),
                ('address', models.CharField(max_length=256, verbose_name='адресс')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=128, verbose_name='Описание продукта'),
        ),
    ]