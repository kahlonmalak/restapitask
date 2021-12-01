from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .models import Articles

from .serializers import ArticleSerializer
from .serializers import ArticlesSerializer
from .serializers import Generic_newSerializer

# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Generic_new
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articled = Article.objects.all()
        serializer = ArticleSerializer(articled,many=True)
        return Response(serializer.data )
    
    elif request.method == 'POST':
        serializer=ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        articlese = Article.objects.get(pk=pk)
        
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)   
    
    if request.method == 'GET':
        serializer = ArticleSerializer(articlese)
        return Response(serializer.data) 
    
    elif request.method =='PUT':
        serializer=ArticleSerializer(articlese,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        articlese.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
               
        
class ArticlesAPIView(APIView):

    def get(self,request):
        artical = Articles.objects.all()
        serializer = ArticlesSerializer(artical,many=True)
        return Response(serializer.data )
    
    def post(self,request):
        serializer=ArticlesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

 
class ArticlesDetail(APIView):
    def get_object(self,id):
        try:
            return Articles.objects.get(id=id)
        except Articles.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   
        
        
    def get(self,request,id):
            new_article=self.get_object(id)
            serializer = ArticlesSerializer(new_article)
            return Response(serializer.data) 
            
    def put(self,request,id):
            new_article=self.get_object(id)
            serializer=ArticlesSerializer(new_article,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
            new_article=self.get_object(id)
            new_article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
               
        
            
class GenericAPIView(
                generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                ):
    
    serializer_class = Generic_newSerializer
    queryset =  Generic_new.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return self.list(request)
            
    def post(self,request):
       return self.create(request)


    
    
class GenAPIView(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):

    serializer_class = Generic_newSerializer
    queryset = Generic_new.objects.all()
    # authentication_classes = [SessionAuthentication , BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
            
    
    def put (self,request,id=None):
        return self.update(request,id)
    
    
    def delete(self,request,id):
        return self.destroy(request,id)




    # def create(self, request):






    
        
    
    
        
       
    


    
    
            
        
        
    