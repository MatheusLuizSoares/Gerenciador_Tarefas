from django.db import models

class Todo(models.Model):
   title= models.CharField(max_length=100,null=False,blank=False)
   created_at= models.DateTimeField(auto_now_add=True,null=False, blank=False)
   dealine=models.DateField(null=False,blank=False)
   finished=models.DateField(null=True)