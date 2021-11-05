from rest_framework import serializers
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from candidates.models import Candidate 
from drf_yasg.utils import swagger_auto_schema
from .serializers import CandidateSerializer

class CandidateListView(APIView):
	"""
	List all candidate or create
	"""
	@swagger_auto_schema(responses={200: CandidateSerializer(many=True)})
	def get(self, request, format=None):
		candidates = Candidate.objects.all()
		serializer = CandidateSerializer(candidates, many=True)
		return Response(serializer.data)

	@swagger_auto_schema(responses={201: CandidateSerializer()})
	def post(self, request, format=None):
		serializer = CandidateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CandidateDetailView(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_object(self, pk):
		return Candidate.objects.get_by_id(pk)

	
	@swagger_auto_schema(responses={200: CandidateSerializer()})
	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		if snippet is None:
			return Response({"message": "Data not found"}, status=HTTP_404_NOT_FOUND)
		serializer = CandidateSerializer(snippet)
		return Response(serializer.data)

	@swagger_auto_schema(responses={200: CandidateSerializer()})
	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		if snippet is None:
			return Response({"message": "Data not found"}, status=HTTP_404_NOT_FOUND)
		serializer = CandidateSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	@swagger_auto_schema(responses={204: CandidateSerializer()})
	def delete(self, request, pk, format=None):
		snippet = self.get_object(pk)
		if snippet is None:
			return Response({"message": "Data not found"}, status=HTTP_404_NOT_FOUND)
		snippet.delete()
		return Response(status=HTTP_204_NO_CONTENT)





























