from django.contrib import admin
from .models import *
import datetime
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

class BidAdmin(admin.ModelAdmin):
    readonly_fields=['bider','dateCreated']
    def get_form(self,request,obj=None,**kwargs):
        Bid.bider = request.user
        Bid.listing = kwargs.get('id')
        Bid.dateCreated = datetime.datetime.now()
        return super(BidAdmin,self).get_form(request, obj, **kwargs)
    
    def save_model(self,request,obj,**kwargs):
        obj.bider = request.user
        obj.listing = kwargs.get('id')
        obj.save()
        return super(BidAdmin,self).save_model(self,request,obj,**kwargs)

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
admin.site.register(Bid,BidAdmin)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Comment,CommentAdmin)
