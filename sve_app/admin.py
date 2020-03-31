from django.contrib import admin
from sve_app.models import Prime,Sold
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PrimeResource(resources.ModelResource):

    class Meta:
        model = Prime

class PrimeAdmin(admin.ModelAdmin):
    resources_class = PrimeResource
    search_fields = ['author','post__items','post__id',]

    # list_display = ['author','items','price','quantity',]






# Register your models here.
admin.site.register(Prime,PrimeAdmin)
admin.site.register(Sold)