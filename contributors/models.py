from django.db import models
from django.core import validators

agree_validator = validators.RegexValidator(regex='I AGREE', message='You must type "I AGREE"')

class LicenseAgreement(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mailing_address = models.TextField()
    country = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255, null=True, blank=True)
    corporate_contributor_information = models.TextField(null=True, blank=True)
    signature = models.CharField(max_length=255, validators=[agree_validator])
    
