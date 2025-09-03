from django.db import models


PREFIX_CHOICES = [
    ('นาย', 'นาย'),
    ('นาง', 'นาง'), 
    ('นางสาว', 'นางสาว'),
]

class Students(models.Model) :
    stuid = models.AutoField(primary_key=True)
    name_prefix = models.CharField( choices=PREFIX_CHOICES, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.stuid) 
               
    