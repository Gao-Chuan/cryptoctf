# Generated by Django 2.0.3 on 2018-06-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminEdit', '0002_challengeinfo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeinfo',
            name='pt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='challengeinfo',
            name='solvers',
            field=models.TextField(default='{"solvers": []}'),
        ),
    ]
