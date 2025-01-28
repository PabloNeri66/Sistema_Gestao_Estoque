from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=500, verbose_name= 'Nome')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
