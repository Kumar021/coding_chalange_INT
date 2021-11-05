from rest_framework import serializers
from candidates.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

	def validate_working_in_us_shift(self, working_in_us_shift):
		if working_in_us_shift is True or working_in_us_shift is False:
			return working_in_us_shift
		raise serializers.ValidationError("working_in_us_shift must be value true of false.")

	class Meta:
		model = Candidate
		fields = (
				'id',
				'candidate_name',
				'job_role',
				'working_in_us_shift',
				'notice_period'
			)