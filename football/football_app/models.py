from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)  #reference to Team model

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=100)
    league = models.ForeignKey('League', on_delete=models.CASCADE)  #reference to League model
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
    
class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey('Team', related_name='home_matches', on_delete=models.CASCADE)  #reference to Team model
    away_team = models.ForeignKey('Team', related_name='away_matches', on_delete=models.CASCADE)  #reference to Team model
    match_date = models.DateTimeField()
    stadium = models.CharField(max_length=100)
    score_home = models.IntegerField(null=True, blank=True)
    score_away = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} on {self.match_date}'

class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    league_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.league_name
    
class MatchEvent(models.Model):
    EVENT_TYPES = [
        ('GOAL', 'Goal'),
        ('YELLOW_CARD', 'Yellow Card'),
        ('RED_CARD', 'Red Card'),
        ('SUBSTITUTION', 'Substitution'),
        ('FOUL', 'Foul'),
    ]
    
    event_id = models.AutoField(primary_key=True)
    match = models.ForeignKey('Match', on_delete=models.CASCADE)  #reference to Match model
    player = models.ForeignKey('Player', on_delete=models.CASCADE)  #reference to Player model
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_time = models.TimeField()

    def __str__(self):
        return f'{self.event_type} by {self.player} in match {self.match}'
