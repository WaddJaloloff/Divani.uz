# Generated by Django 5.0.6 on 2024-06-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='posts',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
