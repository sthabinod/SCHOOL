# Generated by Django 3.0.11 on 2021-04-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210420_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='date_of_admission',
            field=models.DateField(auto_now=True),
        ),
    ]
