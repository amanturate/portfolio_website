# Generated by Django 2.1.4 on 2018-12-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20181228_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('start_dt', models.DateField()),
                ('end_dt', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
