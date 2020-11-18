from django.contrib import admin

from .models import ApiGuide,SiteInfo,Suggestion,Contact

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('name','email','read','timestamp')

admin.site.register(ApiGuide)
admin.site.register(SiteInfo)
admin.site.register(Contact)
admin.site.register(Suggestion,SuggestionAdmin)