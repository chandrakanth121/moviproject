# Generated by Django 2.2.4 on 2019-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dummimodel',
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