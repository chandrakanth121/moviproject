# Generated by Django 2.2.4 on 2019-09-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.IntegerField()),
                ('moviename', models.CharField(max_length=20)),
                ('heroname', models.CharField(max_length=20)),
                ('heroinname', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
