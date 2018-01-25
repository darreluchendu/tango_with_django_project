from django.contrib import admin
from rango.models import Category,Page
# Register your models here.


class PageInline(admin.TabularInline):
    model = Page
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PageInline]
    list_display = ("name","views","likes")


admin.site.register(Category,CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")

admin.site.register(Page,PageAdmin)