from django.contrib import admin
from .models import ItemSender, ItemDetail, ItemReciever


class ItemDetailInline(admin.TabularInline):
    model = ItemDetail
    raw_id_fields = ['item_sender']


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'quantity','description', 'weight', 'image', 'paid', 'status', 'problem_type', 'item_code', 'date_sent', 'date_recieved']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ItemSender)
class ItemSenderAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'address','postal_code', 'country', 'city', 'date_sent']
    list_filter = ['user', 'country', 'date_sent']
    model = ItemDetail


@admin.register(ItemReciever)
class ItemRecieverAdmin(admin.ModelAdmin):
    list_display = ['sender', 'fullname', 'address','postal_code', 'country', 'city', 'date_created']
    list_filter = ['sender', 'date_created', 'country']
    list_editable = ['date_created', 'country']
