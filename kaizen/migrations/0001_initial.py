# Generated by Django 3.1.5 on 2021-04-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='team_kaizen1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team_kaizen2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team_kaizen3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team_kaizen4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team_kaizen5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='team_kaizen6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('kaizen_teian_hituyou_maisuu', models.IntegerField(default=2)),
                ('nenkan_mokuhyou_kingaku', models.IntegerField(default=0)),
                ('team_member_ninzuu', models.IntegerField(default=0)),
            ],
        ),
    ]