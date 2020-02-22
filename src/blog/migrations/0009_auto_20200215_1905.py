# Generated by Django 3.0.2 on 2020-02-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2_third',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_sec',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
