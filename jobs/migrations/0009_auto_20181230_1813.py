# Generated by Django 2.1.4 on 2018-12-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20181230_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desc_2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc_3',
            field=models.TextField(blank=True, default=''),
        ),
    ]