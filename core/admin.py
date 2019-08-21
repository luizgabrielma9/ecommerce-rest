from django.contrib import admin
from .models import Lojista

# Register your models here.

@admin.register(Lojista)
class LojistaModelAdmin(admin.ModelAdmin):
    pass