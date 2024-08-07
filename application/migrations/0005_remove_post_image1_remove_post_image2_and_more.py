# Generated by Django 5.0.6 on 2024-06-03 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_post_image1_alter_post_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image5',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='application.post')),
            ],
        ),
    ]
