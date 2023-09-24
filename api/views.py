from django.http import HttpResponse
from django.shortcuts import render

from api.serializers import ResumeSerializer, CreateResumeSerializer

from .models import Resume

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def hello_view(request):
	return HttpResponse("HELLO")


class ResumeView(generics.ListAPIView):
	queryset = Resume.objects.all()
	serializer_class = ResumeSerializer


class CreateResumeView(APIView):
	serializer_class = CreateResumeSerializer
	  
	def post(self, request, format=None):
		if not self.request.session.exists(self.request.session.session_key):
			self.request.session.create()
		
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			title = serializer.data.get("title")
			content = serializer.data.get("content")
			type = serializer.data.get("type")
			visible = serializer.data.get("visible")

			host = self.request.session.session_key

			resume = Resume.objects.create(host = host, title=title, 
								  content=content, type=type, 
								  visible=visible)
			return Response(ResumeSerializer(resume).data, status=status.HTTP_200_OK)
		
		return Response({'Bad Request': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)



class GetResumeView(APIView):
	lookup_variable = "code"
	serializer_class = ResumeSerializer

	def get(self, request, format=None):
		code = request.GET.get(self.lookup_variable)

		if code == None:
			return Response({'Bad Request': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)
		
		try:
			resume = Resume.objects.get(code = code)
			data = self.serializer_class(resume).data
			if self.request.session.session_key != data.get('host') and not data.get('visible'):
				return Response({'error': 'Resume is hidden'}, status=status.HTTP_403_FORBIDDEN)
			else:
				data['content'] = resume.content
				return Response(data, status=status.HTTP_200_OK)

		except Resume.DoesNotExist:
			return Response({'Resume not found': 'Invalid Resume Code'}, status=status.HTTP_404_NOT_FOUND)






