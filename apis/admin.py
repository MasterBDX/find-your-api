from django.contrib import admin

from .models import UserApiModel,PostApiModel,CommentApiModel


class UsersAPIAdmin(admin.ModelAdmin):
    search_fields = ['id','username', 'email','full_name','birth_place',
                     'phone_number','address','birthday']

admin.site.register(UserApiModel,UsersAPIAdmin)
admin.site.register(PostApiModel)
admin.site.register(CommentApiModel)