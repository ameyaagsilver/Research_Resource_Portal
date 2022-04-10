from django.contrib import admin
from .models import *

admin.site.register(users)

admin.site.register(resource_logbook)

admin.site.register(resources)

admin.site.register(admins)

admin.site.register(resourceRelatedLinks)

admin.site.register(resourceUpdateLogbook)

admin.site.register(userMessage)