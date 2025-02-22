from django.db import models
from django.utils.translation import gettext_lazy as _


class Module(models.Model):
    feature_name = models.CharField('Page Name', max_length=255)
    feature_code = models.CharField('Page Code', max_length=255, unique=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.feature_name
        
class Translation(models.Model):
    LANGUAGE_CHOICES = [
        ('en',"English"),
        ("zh","Chinese")
    ]
    label = models.CharField("Label Code", max_length=255, null=False, blank=False)
    language = models.CharField("Language", choices=LANGUAGE_CHOICES, null=False, blank=False ,max_length=20)
    value = models.CharField("Language Translation", max_length=255, default=None, null=False, blank=True)
    module = models.ForeignKey(Module, verbose_name=_("Pages"), on_delete=models.CASCADE,null=True)
   

    class Meta:
        ordering = ['id']
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'

    def __str__(self):
        return self.label