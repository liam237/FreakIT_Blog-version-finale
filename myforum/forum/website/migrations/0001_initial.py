# Generated by Django 3.1.6 on 2024-01-17 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.admins')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('activated', models.BooleanField(default=False)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PostMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('closes', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.users')),
            ],
        ),
    ]