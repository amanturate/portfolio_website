# Generated by Django 2.1.4 on 2018-12-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_experience_now'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('desc_1', models.TextField(default='')),
                ('desc_2', models.TextField(default='')),
                ('desc_3', models.TextField(default='')),
                ('start_dt', models.DateField()),
                ('end_dt', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='now',
            field=models.BooleanField(default=False, help_text='Check if you are still in the same company'),
        ),
    ]
