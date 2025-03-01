# Generated by Django 5.1.1 on 2024-09-25 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
