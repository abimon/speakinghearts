from django.contrib import admin
from .models import Article,Poem,Music
from tinymce.widgets import TinyMCE
from django.db import models
class textEditorAdmin(admin.ModelAdmin):
    formfield_overrides = { 
    models.TextField: {'widget': TinyMCE()} #optional, set Textarea attributes `attrs={'rows':2, 'cols':8}`
    }
admin.site.register(Article,textEditorAdmin)
admin.site.register(Poem,textEditorAdmin)
admin.site.register(Music,textEditorAdmin)
