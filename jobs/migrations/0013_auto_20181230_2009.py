# Generated by Django 2.1.4 on 2018-12-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_awards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awards',
            name='url',
        ),
        migrations.AddField(
            model_name='awards',
            name='cert',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
