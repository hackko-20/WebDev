# Generated by Django 3.0.5 on 2020-05-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BucketList', '0015_auto_20200513_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='leader_pin',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
    ]
