from rest_framework import serializers
from snippets.models import Snippet

#------> using Serializer class ---------->

# class SnippetSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     title =serializers.CharField(max_length=100)
#     description=serializers.CharField(max_length=1000)

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):        
#         instance.title = validated_data.get('title', instance.title)
#         instance.description=validated_data.get('description', instance.description)        
#         instance.save()
#         return instance


 # using ModelSerializer class ------->>>>>>>>>>>  
 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'description']    

