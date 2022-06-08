from django.contrib import admin

from mainBot.reqHandler.register import *
from mainBot.reqHandler.label import *
from mainBot.reqHandler.help import *
from mainBot.reqHandler.answer import *
from mainBot.reqHandler.image import *
from mainBot.reqHandler.ecourse import *

# Register your models here.

class user_info_admin(admin.ModelAdmin):
    list_display = ('uid','licenseKey','mdt')
admin.site.register(user_info, user_info_admin)

"""class license_key_admin(admin.ModelAdmin):
    list_display = ('licenseKey')
admin.site.register(license_key, license_key_admin)"""

class label_url_admin(admin.ModelAdmin):
    list_display = ('uid','labelName','url','mdt')
admin.site.register(label_url, label_url_admin)

class global_label_url_admin(admin.ModelAdmin): 
    list_display = ('labelName','url','mdt')
admin.site.register(global_label_url, global_label_url_admin)

class image_cmd_tmp_admin(admin.ModelAdmin):
    list_display = ('uid','cmd','mdt')
admin.site.register(image_cmd_tmp, image_cmd_tmp_admin)
