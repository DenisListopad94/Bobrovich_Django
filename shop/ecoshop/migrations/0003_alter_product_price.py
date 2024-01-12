# Generated by Django 4.2.6 on 2023-11-23 00:02

from django.db import migrations, models
import ecoshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0002_alter_product_options_alter_product_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[ecoshop.models.validate_max_price], verbose_name='цена'),
        ),
    ]
