# Generated by Django 2.0.3 on 2018-06-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminEdit', '0003_auto_20180630_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengeinfo',
            name='attachment',
            field=models.FileField(null=True, upload_to='../media/'),
        ),
    ]
