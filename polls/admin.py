from polls.models import Poll
from polls.models import Choice
from polls.models import Token, Vote, WriteInChoice
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

class TokenAdmin(admin.ModelAdmin):
	list_display = ('token', 'used')

class VoteAdmin(admin.ModelAdmin):
	list_display = ('token','choice')
	readonly_fields = ['token', 'choice']

class WriteInChoiceAdmin(admin.ModelAdmin):
	list_display = ('choice', 'vote')
	readonly_fields = ['choice', 'vote']

admin.site.register(Poll, PollAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(WriteInChoice, WriteInChoiceAdmin)
