# Generated by Django 3.1.5 on 2021-04-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0006_goukakuten_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='goukakuten_in',
            name='tuki',
            field=models.IntegerField(default=1),
        ),
    ]