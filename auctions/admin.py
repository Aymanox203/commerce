from django.contrib import admin
from .models import *
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields=['lister']
    def get_form(self,request,obj=None,**kwargs):
        Listing.lister = request.user
        return super().get_form(request,obj,**kwargs)
    def save_model(self,request,obj,**kwargs):
        obj.lister = request.user
        obj.save()


admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Comment)
