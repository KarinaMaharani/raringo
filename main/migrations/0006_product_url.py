# Generated by Django 5.1.1 on 2024-10-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
