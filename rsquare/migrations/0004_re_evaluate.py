# Generated by Django 5.0 on 2024-06-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsquare', '0003_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Re_evaluate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.IntegerField(default=0)),
                ('mark1', models.IntegerField(default=0)),
                ('mark2', models.IntegerField(default=0)),
                ('mark3', models.IntegerField(default=0)),
            ],
        ),
    ]