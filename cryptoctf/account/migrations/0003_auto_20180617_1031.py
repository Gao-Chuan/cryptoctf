# Generated by Django 2.0.3 on 2018-06-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180617_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
