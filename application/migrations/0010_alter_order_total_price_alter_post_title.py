# Generated by Django 5.0.6 on 2024-06-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_rename_product_orderitem_posts_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
