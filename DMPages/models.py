from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=12)
    Description = models.TextField()
    Date = models.DateField()
    
    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})

