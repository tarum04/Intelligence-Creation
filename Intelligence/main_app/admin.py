from django.contrib import admin
from .models import Record, RecordDetail
# Register your models here.

class RecordDetailInline(admin.TabularInline):
    model = RecordDetail

class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ["masalah"]}),
        (None, {"fields" : ["label"]}),
        (None, {"fields" : ["features"]}),
        (None, {"fields" : ["kategori"]}),
        (None, {"fields" : ["status"]}),
    ]
    inlines = [RecordDetailInline]
    search_fields = ["masalah"]



admin.site.register(Record, RecordAdmin)
