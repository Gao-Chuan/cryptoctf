# Generated by Django 2.0.3 on 2018-07-01 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminEdit', '0004_challengeinfo_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengeinfo',
            name='attachment',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
