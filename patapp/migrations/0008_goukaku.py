# Generated by Django 3.1.5 on 2021-04-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0007_goukakuten_in_tuki'),
    ]

    operations = [
        migrations.CreateModel(
            name='goukaku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuki', models.IntegerField(default=1)),
                ('kijunten_in', models.IntegerField(default=85)),
            ],
        ),
    ]
