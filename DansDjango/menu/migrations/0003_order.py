# Generated by Django 3.1.2 on 2020-12-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_populate2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=200)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
    ]
