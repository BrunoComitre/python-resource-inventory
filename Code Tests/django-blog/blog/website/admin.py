from django.contrib import admin
from .models import Post, Contact


# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']  # 'deleted'
    list_filter = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title', 'categories']
    
    # def get_queryset(self, request):  # utilizando filter expressions para usar o approved, uma consulta filtrada
    #     return Post.objects.filter(deleted=True)
    
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    
admin.site.register(Post, PostsAdmin)
admin.site.register(Contact, ContactsAdmin)
