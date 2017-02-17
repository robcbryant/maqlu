from django.contrib import admin

from .models import Project, Form, FormRecordAttributeType, FormRecordAttributeValue, FormRecordReference, FormType


class FormRecordAttributeTypeInline(admin.TabularInline):
    model = FormRecordAttributeType
    extra = 1

class FormRecordAttributeValueInline(admin.TabularInline):
    model = FormRecordAttributeValue
    extra = 1

    
class FormRecordReferenceInline(admin.TabularInline):
    model = FormRecordReference
    extra = 1
    show_change_link = True
    
class FormTypeInline(admin.TabularInline):
    model = FormType
    extra = 1
    
class FormInline(admin.TabularInline):
    model = Form
    extra = 1

class FormRecordAttributeTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['record_type']}),
    ]
    inlines = [FormRecordAttributeValueInline]
    
class FormRecordAttributeValueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['record_value']}),
    ]
    
class FormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['form_name', 'form_type', 'form_record_attribute_type']}),
    ]
    #attributes = 'form_record_attribute_type'
    inlines = [FormRecordAttributeValueInline]
    search_fields = ['form_name']
    
class FormTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['form_type_name']}),
    ]
    inlines = [FormInline, FormRecordAttributeTypeInline]

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['project_name']}),
        ('Date information', {'fields': ['date_created']}),
    ]
    inlines = [FormTypeInline]   

# class FormRecordReferenceAdmin(admin.ModelAdmin):
    # fieldsets = [
        # (None,               {'fields': ['record_name']}),
        # ('Which Form',       {'fields': ['content_object', 'object_id']}),
    # ]
    
    # list_display = ('form', 'get_form_instance')
    # def get_form_instance(self,obj):
        # return obj.form_name
    # get_form_instance.short_description = "Form Name"
    # get_form_instance.admin_order_field = "Form__record_name"
    
# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormRecordAttributeType, FormRecordAttributeTypeAdmin)
admin.site.register(FormType, FormTypeAdmin)
admin.site.register(FormRecordAttributeValue, FormRecordAttributeValueAdmin)