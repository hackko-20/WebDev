# Generated by Django 3.0.5 on 2020-05-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BucketList', '0016_auto_20200513_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='content',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='member',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
