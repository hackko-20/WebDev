# Generated by Django 3.0.5 on 2020-05-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BucketList', '0032_profile_memberpin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mem_username',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]