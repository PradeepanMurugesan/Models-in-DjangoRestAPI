# Generated by Django 5.1.1 on 2024-09-22 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('league_id', models.AutoField(primary_key=True, serialize=False)),
                ('league_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('tier', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('match_date', models.DateTimeField()),
                ('stadium', models.CharField(max_length=100)),
                ('score_home', models.IntegerField(blank=True, null=True)),
                ('score_away', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MatchEvent',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(choices=[('GOAL', 'Goal'), ('YELLOW_CARD', 'Yellow Card'), ('RED_CARD', 'Red Card'), ('SUBSTITUTION', 'Substitution'), ('FOUL', 'Foul')], max_length=20)),
                ('event_time', models.TimeField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_app.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_app.player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_app.league')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_app.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='football_app.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='football_app.team'),
        ),
    ]