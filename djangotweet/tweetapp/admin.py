from django.contrib import admin
from tweetapp.models import Tweet

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Fullname Groups', {"fields": ["name", "surname"]}),
        ('Nickname Groups', {"fields": ["nickname"]}),
        ('Message Groups', {"fields": ["message"]}),
    ]
    # fields = ['nickname', 'name', 'surname', 'message']
    pass

admin.site.register(Tweet, TweetAdmin)
