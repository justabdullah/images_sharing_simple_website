# Generated by Django 2.2.2 on 2019-06-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190628_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='person.png', upload_to='user/%Y/%m/%d'),
        ),
    ]