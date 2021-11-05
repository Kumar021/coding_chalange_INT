from django.db import models


class CandidateManager(models.Manager):
	""" Candidate Model Manager """
	def get_by_id(self, id):
		obj = None 
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			obj = qs.first()
		return obj

class Candidate(models.Model):
	candidate_name 		= models.CharField(max_length=250)
	job_role 			= models.CharField(max_length=200)
	working_in_us_shift = models.BooleanField(default=False)
	notice_period 		= models.PositiveIntegerField(default=0)

	objects = CandidateManager()

	def __str__(self):
		return str(self.candidate_name)


