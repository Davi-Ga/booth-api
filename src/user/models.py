from django.db import models

class User(models.Model):
    nome=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField(blank=False,null=False)
    senha=models.CharField(max_length=50,blank=False,null=False)
    
    def __str__(self):
        return self.nome
    
