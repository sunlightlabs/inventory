#
# admin.py
#

from django.contrib import admin
from QRInventory.models import Item, Improvement, Depreciation, Fund


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'cost', 'category', 'is_assigned', 'where')
    list_editable = ('user', 'is_assigned', 'where')
    list_filter = ('category', 'is_assigned', 'in_inventory', 'where')
    date_hierarchy = 'date_of_purchase'
#
admin.site.register(Item, ItemAdmin)


class FundAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    date_heirarchy = 'date_added'
#
admin.site.register(Fund, FundAdmin)



