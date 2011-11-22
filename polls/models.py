from django.db import models
import datetime

class Poll(models.Model):
	question = models.CharField(max_length=200)

	def __unicode__(self):
		return self.question


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice


class Voter(models.Model):
	email = models.EmailField()

	def __unicode__(self):
		return self.email


class Vote(models.Model):
	voter = models.ForeignKey(Voter)
	choice = models.ForeignKey(Choice)
