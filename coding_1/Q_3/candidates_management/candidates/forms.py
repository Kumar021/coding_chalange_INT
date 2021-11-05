from django import forms

class CandidatesForm(forms.Form):
	candidate_name 		= forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': "form-control"}))
	job_role 			= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "form-control"}))  
	working_in_us_shift = forms.BooleanField(required=False,initial=False)
	notice_period 		= forms.IntegerField(widget=forms.TextInput(attrs={'class': "form-control"}))    

