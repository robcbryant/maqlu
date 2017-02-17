from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Project(models.Model):
    project_name = models.CharField('Project Name', max_length=50)
    date_created = models.DateTimeField('Date Created')
    def __str__(self):
        return self.project_name

class FormType(models.Model):
    form_type_name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.form_type_name
        

 
class FormRecordAttributeType(models.Model):
    record_type = models.CharField(max_length=50)
    form_type = models.ForeignKey(FormType, on_delete=models.CASCADE)
    def __str__(self):
        return self.record_type
        
class FormRecordReference(models.Model):
    record_name = models.CharField(max_length=50)
    #form_parent = models.ForeignKey(Form, on_delete=models.CASCADE)
        
    #limit = models.Q(app_label='enki', model='form')
    #form_type_parent = models.ForeignKey(ContentType, limit_choices_to=limit)
    #object_id = models.PositiveIntegerField(
    #    null = True,
    #)
    #content_object = GenericForeignKey('form_type_parent', 'object_id')
    
    def __str__(self):
        return self.record_name
        
class Form(models.Model):
    form_name = models.CharField(max_length=50)
    form_type = models.ForeignKey(FormType, on_delete=models.CASCADE)
    form_record_attribute_type = models.ManyToManyField(FormRecordAttributeType)
    #form_parent = models.ForeignKey('self', null=True)
    
    def __str__(self):
        return self.form_name

class FormRecordAttributeValue(models.Model):
    record_value = models.CharField(max_length=50)
    record_attribute_type = models.ForeignKey(FormRecordAttributeType, on_delete=models.CASCADE)
    form = models.ForeignKey(Form);
    def __str__(self):
        return self.record_value

        