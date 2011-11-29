from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll, Token, Vote, WriteInChoice

def display_poll(request, poll, token=None, error_message=None):
	return render_to_response('polls/form.html',
			{
			'poll': poll,
			'token': token,
			'error_message': error_message,
			}, context_instance=RequestContext(request))

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	if request.method == 'GET':
		t = request.GET.get('token', None)
		return display_poll(request, poll=p, token=t)
	try:
		t = Token.objects.get(token=request.POST['token'], poll=p)
	except Token.DoesNotExist:
		return display_poll(request, poll=p, token=None,
						error_message="The poll token is invalid.")
	try:
		v = Vote.objects.get(token=t, choice__poll=p)
		return display_poll(request, poll=p, token=t,
			error_message = ("You can only vote once, and you've already voted"
							" for %s" % v.choice.choice))
	except Vote.DoesNotExist:
		pass
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return display_poll(request, poll=p, token=t,
						error_message="You didn't select a choice.")
	else:
		write_in = None
		if selected_choice.choice == 'Other':
			write_in = request.POST.get('write_in', None)
			if not write_in:
				return display_poll(request, poll=p, token=t,
					error_message="'Other' field can't be blank")

		selected_choice.votes += 1
		selected_choice.save()

		vote = Vote(token=t, choice=selected_choice)
		vote.save()
		t.used = True
		t.save()

		if write_in:
			WriteInChoice.objects.create(choice=write_in, vote=vote)
	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	return HttpResponseRedirect(reverse('poll_thanks'))

