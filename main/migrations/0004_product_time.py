# Generated by Django 5.1.1 on 2024-09-17 13:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]