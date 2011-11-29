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


class Token(models.Model):
	token = models.CharField(max_length=7, unique=True)
	poll = models.ForeignKey(Poll)
	used = models.BooleanField(default=False)

	def __unicode__(self):
		return self.token


class Vote(models.Model):
	token = models.ForeignKey(Token)
	choice = models.ForeignKey(Choice)

	def __unicode__(self):
		return "Token: %s" % self.token.token

class WriteInChoice(models.Model):
	choice = models.CharField(max_length=200)
	vote = models.ForeignKey(Vote)
