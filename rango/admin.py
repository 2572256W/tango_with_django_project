from django.contrib import admin
from rango.models import Category,Page

# admin.site.register(Category)
# admin.site.register(Page)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title','url')
    list_per_page = 20

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views','likes')
    list_per_page = 20

admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)
