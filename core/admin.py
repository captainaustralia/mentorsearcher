from django.contrib import admin

# Register your models here.
from core.models import UserPoll, Technologies, Offer, Request

admin.site.register(UserPoll)
admin.site.register(Technologies)
admin.site.register(Request)
admin.site.register(Offer)
