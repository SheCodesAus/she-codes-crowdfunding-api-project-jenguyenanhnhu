# Generated by Django 4.0.2 on 2022-06-25 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='type',
        ),
    ]
