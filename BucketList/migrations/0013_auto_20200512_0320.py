# Generated by Django 3.0.5 on 2020-05-11 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BucketList', '0012_auto_20200512_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='member_id',
            new_name='memberid',
        ),
    ]
