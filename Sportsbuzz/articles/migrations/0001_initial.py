# Generated by Django 3.2.4 on 2021-07-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=150)),
                ('article_link', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('date_posted', models.DateTimeField()),
                ('img_url', models.TextField()),
            ],
        ),
    ]