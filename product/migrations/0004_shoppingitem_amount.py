# Generated by Django 4.2.9 on 2024-02-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_shoppingitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='amount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
