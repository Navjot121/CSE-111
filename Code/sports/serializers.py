from rest_framework import serializers

from sports.models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class InjurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Injury
        fields = "__all__"


class PlayerPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerPosition
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStats
        fields = "__all__"


class PlayerInjuriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInjuries
        fields = "__all__"


class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = "__all__"

