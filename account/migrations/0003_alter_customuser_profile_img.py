# Generated by Django 4.2.2 on 2023-07-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.ImageField(blank=True, default='images/default-avatar-profile-icon-symbol-for-website-vector-46547084.jpg', null=True, upload_to='user_profiles/'),
        ),
    ]