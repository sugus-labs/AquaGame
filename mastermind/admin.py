from django.contrib import admin
from mastermind.models import Ball, Participant

class ParticipantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Participant',{'fields': ['nick_name', 'time_needed']}),
    ]
    list_display = ('nick_name', 'time_needed')
    list_filter = ['date_created']
    search_fields = ['nick_name', 'time_needed']

admin.site.register(Participant, ParticipantAdmin)

class BallAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ball',{'fields': ['colour', 'liquid_contained', 'liquid_contained_density']}),
    ]
    list_display = ('colour', 'liquid_contained', 'liquid_contained_density', 'date_created')
    list_filter = ['date_created']
    search_fields = ['liquid_contained']

admin.site.register(Ball, BallAdmin)