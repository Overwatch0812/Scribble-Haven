# Generated by Django 4.2.2 on 2023-07-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0007_upload_image_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]