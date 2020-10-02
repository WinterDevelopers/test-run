from django.contrib import admin
from demoapp.models import Topic, AccessRecord, WebPage, User, UserProfileInfo


# Register your models here
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(User)
admin.site.register(UserProfileInfo)
