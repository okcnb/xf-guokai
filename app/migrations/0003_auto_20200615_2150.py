# Generated by Django 2.0.1 on 2020-06-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.FileField(max_length=50, upload_to='', verbose_name='密码'),
        ),
    ]
