# Generated by Django 4.0.2 on 2022-08-27 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='is_open',
            new_name='is_diversity',
        ),
        migrations.AddField(
            model_name='project',
            name='is_education',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_health',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_human_rights',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_other',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_sustainability',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='is_technology',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.CharField(choices=[('Ideation', 'Ideation Stage'), ('Need Funds', 'Fundraising and accepting all forms of help'), ('Behind', 'Behind'), ('On Track', 'On Track'), ('Ahead of Schedule', 'Ahead of Schedule'), ('Complete', 'Complete'), ('Abandoned', 'Abandoned')], default=False, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pledge',
            name='comment',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='type',
            field=models.CharField(choices=[('$', 'Money'), ('Time', 'Volunteering Time'), ('Advice', 'Advice'), ('Resources', 'Resources'), ('Other', 'Other')], max_length=20),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
                ('progress', models.CharField(choices=[('Ideation', 'Ideation Stage'), ('Need Funds', 'Fundraising and accepting all forms of help'), ('Behind', 'Behind'), ('On Track', 'On Track'), ('Ahead of Schedule', 'Ahead of Schedule'), ('Complete', 'Complete'), ('Abandoned', 'Abandoned')], max_length=20)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('next_update', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='projects.project')),
            ],
        ),
    ]
