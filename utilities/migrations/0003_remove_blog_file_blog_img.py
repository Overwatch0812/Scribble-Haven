# Generated by Django 4.2.2 on 2023-07-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0002_alter_blog_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='file',
        ),
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
