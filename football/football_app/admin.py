from django.contrib import admin
from .models import Player,Match,Team,MatchEvent,League
# Register your models here
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(MatchEvent)
admin.site.register(League)
