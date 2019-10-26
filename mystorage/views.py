from django.shortcuts import render
## serializers, status 추가
from rest_framework import viewsets, serializers, status
## Album, Files 모델 추가.
from .models import Essay, Album, Files
## serializer 추가.
from .serializers import EssaySerializer, AlbumSerializer, FileSerializer
from rest_framework.filters import SearchFilter
## Response와 Parser들 추가.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    
    #SearchFilter 설정
    filter_backends = [SearchFilter]
    search_fields = ('title','body')
    
    ## 수정
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    # queryset 추가
    def get_queryset(self):
        qs = super().get_queryset()
        
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        return qs

## viewset들 추가.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
    ## 파일 업로드를 위한 parser_classes와 post 오버라이딩.
    # parser_class
    parser_classes = (MultiPartParser, FormParser)

    # create()
    def post(self, request, *args, **kwargs):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
status=status.HTTP_400_BAD_REQUEST)