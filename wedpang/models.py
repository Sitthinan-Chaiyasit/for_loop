from django.db import models

class Students(models.Model):
    PREFIX_CHOICES = [
        ('นาย', 'นาย'),
        ('นางสาว', 'นางสาว'),
        ('นาง', 'นาง'),
    ]
    
    stuid = models.BigIntegerField(unique=True)  # เปลี่ยนเป็น BigIntegerField เพื่อรองรับตัวเลขขนาดใหญ่
    name_prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.stuid} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

