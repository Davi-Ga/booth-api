from django.db import models

class Booth(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    name=models.CharField(max_length=50,blank=False, null=False)
    booth=models.ForeignKey(Booth, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id