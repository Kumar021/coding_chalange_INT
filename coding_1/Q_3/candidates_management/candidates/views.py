import uuid
from django.shortcuts import render, redirect
from .models import Candidate
from .forms import CandidatesForm
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView



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


candidate_list = [
			{
				'id':1,
				'candidate_name': 'RAj Kr',
				'job_role': 'SE-1',
				'working_in_us_shift': 'true',
				'notice_period': 24
			},
			{
				'id':2,
				'candidate_name': 'Ramesh Kr',
				'job_role': 'SE-2',
				'working_in_us_shift': 'true',
				'notice_period': 30
			},
			{
				'id':3,
				'candidate_name': 'Pradive Kr',
				'job_role': 'QA-1',
				'working_in_us_shift': 'false',
				'notice_period': 35
			},
		]

class CandidateView(View):
	"""
	Candidate List and Craete
	"""
	def get(self, request, *args, **kwargs):
		
		context = {'candidate_list': candidate_list}
		return render(request, "candidates/candidates_list.html", context)

	def post(self, request, *args, **kwargs):
		data = {
				'id':uuid.uuid4(),
				'candidate_name': request.POST['candidate_name'],
				'job_role': request.POST['job_role'],
				'working_in_us_shift': request.POST['working_in_us_shift'],
				'notice_period': request.POST['notice_period']
			}
		candidate_list.append(data)

		context = {'candidate_list': candidate_list}
		return render(request, "candidates/candidates_list.html", context)
	

class CandidateUpdateView(View):
	"""
	Candidate Update
	"""
	def get(self, request, id, *args, **kwargs):
		initial = {}
		for i in range(len(candidate_list)):
			if str(candidate_list[i].get('id')) == id:
				initial={
					'candidate_name': candidate_list[i].get('candidate_name'),
					'working_in_us_shift': candidate_list[i].get('working_in_us_shift'),
					'job_role': candidate_list[i].get('job_role'),
					'notice_period': candidate_list[i].get('notice_period'),
				}
		form = CandidatesForm(initial=initial)
		context = {'form': form, 'id': id}
		return render(request, "candidates/candidates_update.html", context)

	def post(self, request, id, *args, **kwargs):
		for i in range(len(candidate_list)):
			if str(candidate_list[i].get('id')) == id:
				initial={
					'candidate_name': request.POST.get('candidate_name'),
					'working_in_us_shift': request.POST.get('working_in_us_shift'),
					'job_role': request.POST.get('job_role'),
					'notice_period': request.POST.get('notice_period'),
				}
				candidate_list[i].update(initial)

		context = {'candidate_list': candidate_list}
		return render(request, "candidates/candidates_list.html", context)


class CandidateDeleteView(View):
	"""
	Candidate Delete
	"""
	def get(self, request, id, *args, **kwargs):
		initial = {}
		for i in range(len(candidate_list)):
			if str(candidate_list[i].get('id')) == id:
				del candidate_list[i]
		
		context = {'candidate_list': candidate_list}
		return render(request, "candidates/candidates_list.html", context)
