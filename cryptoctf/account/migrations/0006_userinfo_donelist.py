# Generated by Django 2.0.3 on 2018-06-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180619_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='doneList',
            field=models.TextField(default='{"doneList": []}'),
        ),
    ]
