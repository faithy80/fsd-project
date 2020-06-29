# Generated by Django 3.0.7 on 2020-06-26 10:28

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Product name')),
                ('product_description', models.CharField(max_length=200, verbose_name='Product description')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_image', models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='product_images', verbose_name='Product image')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
