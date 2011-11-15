from django.db import models

class Member(models.Model):
    """
    Someone who's interested in the project.
    """
    email = models.EmailField(max_length=200)
    notes = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email

class PilotRecommendation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    place = models.CharField(max_length=250)
    about = models.TextField()
    photo = models.ImageField(upload_to='pilot_images')
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return (self.place + ' - ' + self.email)
