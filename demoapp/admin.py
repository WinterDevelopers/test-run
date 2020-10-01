from django.contrib import admin
from demoapp.models import Topic, AccessRecord, WebPage, User, UserProfileInfo


# Register your models here
@admin.register(Topic,AccessRecord,WebPage,User,UserProfileInfo)
class PersonAdmin(admin.ModelAdmin):
    pass
