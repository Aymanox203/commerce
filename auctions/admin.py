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
        if obj.image==None:
            obj.image='auctions/Camera.jpg'
        obj.save()
        return super(ListingAdmin,self).save_model(self,request,obj,**kwargs)

class CommentAdmin(admin.ModelAdmin):
    readonly_fields=['commenter']
    def get_form(self,request,obj=None,**kwargs):
        Comment.commenter = request.user
        Comment.listing = kwargs.get('id')
        return super().get_form(request,obj,obj,**kwargs)
    def save_model(self,request,obj,**kwargs):
        obj.commenter = request.user
        obj.listing = kwargs.get('id')
        return super().save_model(self,request,obj,**kwargs)

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Comment,CommentAdmin)
