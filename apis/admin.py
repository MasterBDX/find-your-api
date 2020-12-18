from django.contrib import admin

from .models import UserApiModel,PostApiModel,CommentApiModel


class UsersAPIAdmin(admin.ModelAdmin):
    search_fields = ['id','username', 'email','full_name','birth_place',
                     'phone_number','address','birthday']

class PostsAPIAdmin(admin.ModelAdmin):
    list_display = ('title','id','author_id','author_name')


class CommentsAPIAdmin(admin.ModelAdmin):
    list_display = ('id','post_id','user_id',
                    'username','created_at')

admin.site.register(UserApiModel,UsersAPIAdmin)
admin.site.register(PostApiModel,PostsAPIAdmin)
admin.site.register(CommentApiModel,CommentsAPIAdmin)