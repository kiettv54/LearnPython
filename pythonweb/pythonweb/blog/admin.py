from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    lis_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title']
admin.site.register(Post,PostAdmin)