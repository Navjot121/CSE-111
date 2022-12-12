from django.contrib import admin
from .models import Injury, Player, PlayerPosition, Team, Coach, PlayerStats, PlayerInjuries, TeamStats


admin.site.register([Injury, Player, PlayerPosition, Team, Coach, PlayerStats, PlayerInjuries, TeamStats])
