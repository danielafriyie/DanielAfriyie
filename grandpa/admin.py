from django.contrib import admin
from . import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'intro', 'headline', 'date')
    list_display_links = ('id', 'intro')


class MyWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'work_title', 'work_link', 'date')
    list_display_links = ('id', 'work_title')
    list_filter = ('date',)
    search_fields = ('id', 'work_title', 'work_link', 'date')
    list_per_page = 25


admin.site.register(models.MyProfile, ProfileAdmin)
admin.site.register(models.MyWorkPortfolio, MyWorkAdmin)
