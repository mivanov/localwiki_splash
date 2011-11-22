from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll, Voter, Vote

def form(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/form.html', {'poll': p}, context_instance=RequestContext(request))


def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		voter = Voter.objects.get(email=request.POST['email'])
	except Voter.DoesNotExist:
		return render_to_response('polls/form.html', {
			'poll': p,
			'error_message': "The email you entered is not in our records.",		
		}, context_instance = RequestContext(request))
	try:
		v = Vote.objects.get(voter=voter, choice__poll=p)
		return render_to_response('polls/form.html', {
			'poll': p,
			'error_message': "You can only vote once, and you've already voted for %s" % v.choice.choice,
		}, context_instance = RequestContext(request))
	except Vote.DoesNotExist:
		pass
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render_to_response('polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		}, context_instance = RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		vote = Vote(voter=voter, choice=selected_choice)
		vote.save()
	# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_thanks'))
