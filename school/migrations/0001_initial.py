# Generated by Django 3.2.3 on 2021-05-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='img_default.jpg', upload_to='static/images/partner')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('image', models.ImageField(default='default.jpg', upload_to='static/images/principal')),
            ],
            options={
                'verbose_name_plural': 'Principal',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, default='default_img.jpg', null=True, upload_to='static/images/school')),
                ('philosophy', models.CharField(max_length=200)),
                ('academic_principal', models.CharField(max_length=200)),
                ('facilities', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'School',
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
    ]
