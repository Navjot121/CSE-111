from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("get-all-player/", GetAllPlayers.as_view(), name='get-all-player'),
    path("get-all-coach/", GetAllCoach.as_view(), name='get-all-coach'),
    path("get-all-injury/", GetAllInjury.as_view(), name='get-all-injury'),
    path("get-all-player-position/", GetAllPlayerPosition.as_view(), name='get-all-player-position'),
    path("get-all-team/", GetAllTeam.as_view(), name='get-all-team'),
    path("get-all-team-stats/", GetAllTeamStats.as_view(), name='get-all-team-stats'),
    path("get-all-player-injuries/", GetAllPlayerInjuries.as_view(), name='get-all-player-injuries'),
    path("get-all-player-stats/", GetAllPlayerStats.as_view(), name='get-all-player-stats'),

    path("add-coach/", AddCoach.as_view(), name='add-coach'),
    path("add-injury/", AddInjury.as_view(), name='add-injury'),
    path("add-player-position/", AddPlayerPosition.as_view(), name='add-player-position'),
    path("add-team/", AddTeam.as_view(), name='add-team'),
    path("add-team-stats/", AddTeamStats.as_view(), name='add-team-stats'),
    path("add-player/", AddPlayer.as_view(), name='add-player'),
    path("add-player-injuries/", AddPlayerInjuries.as_view(), name='add-player-injuries'),
    path("add-player-stats/", AddPlayerStats.as_view(), name='add-player-stats'),

]
