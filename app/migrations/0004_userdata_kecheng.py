# Generated by Django 2.0.1 on 2020-06-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200615_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='kecheng',
            field=models.FileField(max_length=50, null=True, upload_to='', verbose_name='课程'),
        ),
    ]