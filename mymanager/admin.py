from django.contrib import admin
from .models import Trainer, Course, Announcement

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Course)
admin.site.register(Announcement)
