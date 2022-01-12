from rest_framework import serializers
from . models import Article


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ['id','title', 'author', 'email']

# class ArticleSerializer(serializers.Serializer):
# 	title = serializers.CharField(max_length=100)
# 	author = serializers.CharField(max_length=100)
# 	email = serializers.EmailField(max_length=100)
# 	date = serializers.DateTimeField()

# 	def create(self, validated_data):
# 		return Article.objects.create(validated_data)
