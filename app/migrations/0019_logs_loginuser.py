# Generated by Django 2.2.1 on 2020-06-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200618_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='loginUser',
            field=models.CharField(max_length=50, null=True, verbose_name='操作用户'),
        ),
    ]