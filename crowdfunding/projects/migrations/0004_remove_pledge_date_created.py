# Generated by Django 4.0.2 on 2022-07-10 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_pledge_date_created_alter_pledge_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='date_created',
        ),
    ]
