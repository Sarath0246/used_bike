# Generated by Django 3.2.15 on 2022-10-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_sales_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('approved', 'approved'), ('pending', 'pending'), ('sold-out', 'sold-out'), ('you bought this product', 'you bought this product')], default='pending', max_length=120),
        ),
    ]
