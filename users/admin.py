from django.contrib import admin

from users.models import CustomUser, Saved
from django.contrib.auth.models import Group


admin.site.register(CustomUser)
admin.site.unregister(Group)
admin.site.register(Saved)