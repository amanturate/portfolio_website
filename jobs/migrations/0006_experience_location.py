# Generated by Django 2.1.4 on 2018-12-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20181230_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
    ]
