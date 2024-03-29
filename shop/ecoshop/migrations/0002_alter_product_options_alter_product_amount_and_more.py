# Generated by Django 4.2.6 on 2023-11-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FR', 'Fruit'), ('VG', 'Vegetable'), ('ML', 'Milk'), ('MT', 'Meat'), ('TC', 'Tea and Coffee'), ('FS', 'Fish'), ('AL', 'Alcohol')], max_length=2, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='delivery_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата поставки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='perfect product', max_length=100, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='цена'),
        ),
    ]
