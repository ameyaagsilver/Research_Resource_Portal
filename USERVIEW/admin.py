from django.contrib import admin
from .models import *

admin.site.register(users)

admin.site.register(resource_logbook)

admin.site.register(resources)

admin.site.register(admins)

admin.site.register(tender)

admin.site.register(committee)

admin.site.register(committee_members)

admin.site.register(resourceRelatedLinks)
