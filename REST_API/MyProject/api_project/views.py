from django.shortcuts import render
from . models import Article
from rest_framework.views import APIView
from . serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
#from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser 

# Create your views here.

class ArticleAPIView(APIView):
	def get(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ArticleSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

class ArticleDetail(APIView):

	def get_object(self, id):
		try:
			return Article.objects.get(id=id)
		except Article.DoesNotExist:
			return Response(status=status.HTTP_400_NOT_FOUND)

	def get(self, request, id):
		article = self.get_object(id)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	def put(self, request, id):
		article = self.get_object(id)
		serializer = ArticleSerializer(article, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request,id):
		article = self.get_object(id)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)







# def article_list(request):
# 	if request.method == 'GET':
# 		articles = Article.objects.all()
# 		serializer = ArticleSerializer(articles, many=True)
# 		return JsonResponse(serializer.data, safe=False)
		
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = ArticleSerializer(data=data)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data,status=201)
# 		return JsonResponse(serializer.data, status=400)	
		