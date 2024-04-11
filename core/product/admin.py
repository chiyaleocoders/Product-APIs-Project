from django.contrib import admin
from .models import *
# Register your models here.
@ admin.register(Tbl_Tax_M)
class Tbl_Tax_MAdmin(admin.ModelAdmin):
    list_display =Tbl_Tax_M.DisplayList

    