from django.contrib import admin

from Insta.models import Post, InstaUser, Like, UserConnection, Comment
# Register your models here.

admin.site.register(Post) #需要注册models里面的类 ，table
admin.site.register(InstaUser)
admin.site.register(Like)
admin.site.register(UserConnection)
admin.site.register(Comment)