# Generated by Django 2.0.3 on 2018-06-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180617_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='rank',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
    ]
