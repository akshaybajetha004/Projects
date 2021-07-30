# Generated by Django 3.2.4 on 2021-07-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AddField(
            model_name='article',
            name='article_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
        ),
    ]