from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, Game, Comment


class GameAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'about'


admin.site.register(Contact)
admin.site.register(Game, GameAdmin)
admin.site.register(Comment)
