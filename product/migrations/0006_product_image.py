# Generated by Django 4.2.9 on 2024-02-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_shoppingitem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='product_images/'),
        ),
    ]
