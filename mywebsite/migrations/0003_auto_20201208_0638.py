# Generated by Django 3.1.2 on 2020-12-08 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20201208_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='annoucement',
            new_name='announcement',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 8, 6, 38, 49, 706311, tzinfo=utc)),
        ),
    ]
