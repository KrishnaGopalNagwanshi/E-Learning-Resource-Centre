from django.contrib import admin

# Register your models here.
from links.models import *
from pdfs.models import *
from videos.models import *
from .models import *
class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(linksmodels,MyModelAdmin)
admin.site.register(pdfsmodels,MyModelAdmin)
admin.site.register(videosmodels,MyModelAdmin)
admin.site.register(adprofile,MyModelAdmin)
admin.site.register(recentlog,MyModelAdmin)
