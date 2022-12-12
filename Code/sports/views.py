from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView

from sports.serializers import *


class HomeView(TemplateView):
    template_name = 'sports/home.html'


class GetAllPlayers(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class GetAllCoach(ListAPIView):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()


class GetAllInjury(ListAPIView):
    serializer_class = InjurySerializer
    queryset = Injury.objects.all()


class GetAllPlayerPosition(ListAPIView):
    serializer_class = PlayerPositionSerializer
    queryset = PlayerPosition.objects.all()


class GetAllTeam(ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class GetAllTeamStats(ListAPIView):
    serializer_class = TeamStatsSerializer
    queryset = TeamStats.objects.all()


class GetAllPlayerInjuries(ListAPIView):
    serializer_class = PlayerInjuriesSerializer
    queryset = PlayerInjuries.objects.all()


class GetAllPlayerStats(ListAPIView):
    serializer_class = PlayerStatsSerializer
    queryset = PlayerStats.objects.all()


class GetAllStarPlayers(ListAPIView):
    serializer_class = Player
    queryset = PlayerStats.objects.all()


########################################################################


class AddCoach(CreateView):
    model = Coach
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'


class AddInjury(CreateView):
    model = Injury
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'


class AddPlayerPosition(CreateView):
    model = PlayerPosition
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'


class AddTeam(CreateView):
    model = Team
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'

    def get_form(self, form_class=None):
        form = super(AddTeam, self).get_form(form_class)
        form.fields['coaches'].required = False
        return form


class AddTeamStats(CreateView):
    model = TeamStats
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'


class AddPlayer(CreateView):
    model = Player
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'

    def get_form(self, form_class=None):
        form = super(AddPlayer, self).get_form(form_class)
        form.fields['injuries'].required = False
        return form


class AddPlayerInjuries(CreateView):
    model = PlayerInjuries
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'


class AddPlayerStats(CreateView):
    model = PlayerStats
    fields = '__all__'
    template_name = 'sports/common_form.html'
    success_url = '/'



