from django.contrib import admin

from .models import ApiGuide,SiteInfo,Suggestion

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('name','email','read','timestamp')

admin.site.register(ApiGuide)
admin.site.register(SiteInfo)
admin.site.register(Suggestion,SuggestionAdmin)