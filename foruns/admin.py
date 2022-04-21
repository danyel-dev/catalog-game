from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Forum


class ForumAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'    


admin.site.register(Forum, ForumAdmin)
