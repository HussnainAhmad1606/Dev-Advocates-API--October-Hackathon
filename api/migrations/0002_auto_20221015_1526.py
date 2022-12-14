# Generated by Django 3.1.4 on 2022-10-15 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('youtube', models.URLField()),
                ('twitter', models.URLField()),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='advocate',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='advocate',
            name='profile_pic',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='advocate_since',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('logo', models.URLField()),
                ('summary', models.CharField(max_length=200)),
                ('advocates_name', models.ManyToManyField(to='api.Advocate')),
            ],
        ),
        migrations.AddField(
            model_name='advocate',
            name='company_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AddField(
            model_name='advocate',
            name='links',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='api.link'),
        ),
    ]
