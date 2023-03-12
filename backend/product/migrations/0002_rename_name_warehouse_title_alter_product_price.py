# Generated by Django 4.1.7 on 2023-03-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouse',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена товара: '),
        ),
    ]