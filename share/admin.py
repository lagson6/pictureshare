from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from share.models import *

class PhotoInline (admin.StackedInline):
    model = Photo.albums.through
    extra = 1

class AlbumAdmin (admin.ModelAdmin):
    inlines = [PhotoInline]

class PhotoAdmin (admin.ModelAdmin):
    inlines = [PhotoInline]
    exclude = ('albums',)

class UserAccountInline (admin.StackedInline):
    model = UserAccount

class MyUserAdmin (UserAdmin):
    inlines = [UserAccountInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)