# Generated by Django 5.0.6 on 2024-06-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_age', models.IntegerField()),
                ('user_gender', models.CharField(choices=[('a', 'Male'), ('b', 'Female'), ('c', 'Other')], max_length=20)),
                ('user_scoolname', models.CharField(max_length=1024)),
            ],
        ),
    ]