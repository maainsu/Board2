from django.contrib import admin
from board.models import board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "content")
    
admin.site.register(board, BoardAdmin)