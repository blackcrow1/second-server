from django.contrib import admin
from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display=('title', 'name', 'contents', 'created')

admin.site.register(Snippet, SnippetAdmin)