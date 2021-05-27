from django.contrib import admin
from .models import dashitem, loginfo

# Register your models here.
class dashitems(admin.ModelAdmin):
    list_display = ('name', 'memo', 'enable', 'asdefault', 'owner', 'menuindex')


class loginfos(admin.ModelAdmin):
    list_display = ('user', 'logdate', 'action', 'status', 'addr', 'os', 'osver', 'browser', 'browserver', 'device', 'memo')


# register table for admin management
admin.site.register(dashitem, dashitems)
admin.site.register(loginfo, loginfos)
