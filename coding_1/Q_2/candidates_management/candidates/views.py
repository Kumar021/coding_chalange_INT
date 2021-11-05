from django.shortcuts import render, redirect
from .models import Candidate
from .forms import CandidatesForm

def candidates_list_view(request):
	candidate_qs = Candidate.objects.all()
	context = {
		'candidate_qs': candidate_qs
	}
	return render(request, "candidates/candidates_list.html", context)


def candidates_delete_view(request, id):
	candidate_obj = Candidate.objects.filter(id=id).delete()
	return redirect('candidates:list')

def candidates_create_view(request):
	if request.method == "POST":
		form = CandidatesForm(request.POST)
		if form.is_valid():
			candidate_name = form.cleaned_data['candidate_name']
			job_role = form.cleaned_data['job_role']
			working_in_us_shift = form.cleaned_data['working_in_us_shift']
			notice_period = form.cleaned_data['notice_period']
			c = Candidate.objects.create(
				candidate_name=candidate_name,
				job_role=job_role,
				working_in_us_shift=working_in_us_shift,
				notice_period=notice_period
			)
			return redirect('candidates:list')
	context = {'form': CandidatesForm}
	return render(request, 'candidates/candidates_create.html', context)


def candidates_update_view(request, id):
	candidate_obj = Candidate.objects.get_by_id(id)
	if request.method == "POST":
		form = CandidatesForm(request.POST)
		if form.is_valid():
			candidate_name = form.cleaned_data['candidate_name']
			job_role = form.cleaned_data['job_role']
			working_in_us_shift = form.cleaned_data['working_in_us_shift']
			notice_period = form.cleaned_data['notice_period']
			can_obj = Candidate.objects.filter(id=id).update(
					candidate_name=candidate_name,
					job_role=job_role,
					working_in_us_shift=working_in_us_shift,
					notice_period=notice_period
				)
			return redirect('candidates:list')
	
	initial={
		'candidate_name': candidate_obj.candidate_name,
		'job_role': candidate_obj.job_role,
		'working_in_us_shift': candidate_obj.working_in_us_shift,
		'notice_period': candidate_obj.notice_period,
	}
	form = CandidatesForm(initial=initial)
	context = {'form': form, 'id': id}
	return render(request, 'candidates/candidates_update.html', context)
	