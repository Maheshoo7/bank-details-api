from django.contrib import admin
from .models import Branch

class BranchAdmin(admin.ModelAdmin):
    list_display = ['bank', 'ifsc', 'city', 'state']


admin.site.register(Branch, BranchAdmin)

