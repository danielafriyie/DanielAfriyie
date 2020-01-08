from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'intro', 'headline', 'date')
    list_display_links = ('id', 'intro')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_title', 'work_link', 'date')
    list_display_links = ('id', 'work_title')
    list_filter = ('date',)
    search_fields = ('id', 'work_title', 'work_link', 'date')
    list_per_page = 25


admin.site.register(models.UserProfile, UserAdmin)
admin.site.register(models.WorkPortfolio, WorkAdmin)
