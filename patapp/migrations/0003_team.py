# Generated by Django 3.1.5 on 2021-04-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0002_kakutuki_a_kakutuki_b_kakutuki_c_kakutuki_d_kakutuki_e'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
    ]
