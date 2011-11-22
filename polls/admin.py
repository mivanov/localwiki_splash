from polls.models import Poll
from polls.models import Choice
from polls.models import Voter, Vote
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 10

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				 {'fields':['question']}),
	]
	inlines = [ChoiceInline]
	list_display   = ('question',)
	search_fields  = ['question']

class VoterAdmin(admin.ModelAdmin):
	list_display = ('email',)

class VoteAdmin(admin.ModelAdmin):
	list_display = ('voter','choice')
	readonly_fields = ['voter', 'choice']

admin.site.register(Poll, PollAdmin)
admin.site.register(Voter, VoterAdmin)
admin.site.register(Vote, VoteAdmin)
