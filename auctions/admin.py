from django.contrib import admin
from .models import *
import datetime
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields=['lister']
  

class BidAdmin(admin.ModelAdmin):
    readonly_fields=['bider','dateCreated']
   

class CommentAdmin(admin.ModelAdmin):
    readonly_fields=['commenter']
 

admin.site.register(User)
admin.site.register(Bid,BidAdmin)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Comment,CommentAdmin)
