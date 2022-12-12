from django.db import models


class Coach(models.Model):
    C_name = models.CharField(max_length=50)
    C_coachID = models.CharField(max_length=50)
    C_gamesWon = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.C_coachID} - {self.C_name}"


class Injury(models.Model):
    I_name = models.CharField(max_length=50)
    I_location = models.CharField(max_length=50)
    I_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.I_name} - {self.I_type}"


class PlayerPosition(models.Model):
    PP_positionName = models.CharField(max_length=50)
    PP_offense = models.CharField(max_length=50)
    PP_defense = models.CharField(max_length=50)
    PP_specialTeams = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.PP_positionName} - {self.PP_specialTeams}"


class Team(models.Model):
    T_name = models.CharField(max_length=50)
    T_teamID = models.CharField(max_length=50)
    coaches = models.ManyToManyField(Coach, related_name='teams')
    players = models.ManyToManyField('Player', related_name='teams', through='PlayerStats')

    def __str__(self):
        return f"{self.T_teamID} - {self.T_name}"


class TeamStats(models.Model):
    TS_team = models.ForeignKey(Team, related_name='team_stats', on_delete=models.CASCADE)
    TS_totalTouchDowns = models.CharField(max_length=50)
    TS_totalYards = models.CharField(max_length=50)
    TS_rushingYards = models.CharField(max_length=50)
    TS_passingYards = models.CharField(max_length=50)
    TS_turnOvers = models.CharField(max_length=50)

    def __str__(self):
        return f"Stats for team -> {self.TS_team}"


class Player(models.Model):
    P_name = models.CharField(max_length=50)
    P_teamName = models.CharField(max_length=50)
    P_playerNumber = models.CharField(max_length=50)
    P_position = models.ForeignKey(PlayerPosition, related_name='players', on_delete=models.CASCADE)
    injuries = models.ManyToManyField(Injury, related_name='players', through='PlayerInjuries')

    def __str__(self):
        return f"{self.id}. {self.P_playerNumber} - {self.P_name}"


class PlayerInjuries(models.Model):
    player = models.ForeignKey(Player, related_name='player_injuries', on_delete=models.CASCADE)
    injury = models.ForeignKey(Injury, related_name='player_injuries', on_delete=models.CASCADE)
    Date_injured = models.DateField()
    Return_date = models.DateField()

    def __str__(self):
        return f"{self.player} - {self.injury}"


class PlayerStats(models.Model):
    PS_team = models.ForeignKey(Team, related_name='player_stats', on_delete=models.CASCADE)
    PS_player = models.ForeignKey(Player, related_name='player_stats', on_delete=models.CASCADE)
    PS_passingYards = models.CharField(max_length=50)
    PS_rushingYards = models.CharField(max_length=50)
    PS_receivingYards = models.CharField(max_length=50)
    PS_numberOfTurnOvers = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.PS_team} - {self.PS_player}"
