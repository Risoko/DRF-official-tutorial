from django.shortcuts import get_object_or_404

from rest_framework import mixins, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    
#class SnippetList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)

#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)


#class SnippetDetail(mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    generics.GenericAPIView):
#    queryset = Snippet.objects.all()
#    serializer_class = SnippetSerializer

#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)

#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)

#class SnippetList(APIView):
    
#    def get(self, request, format=None):
#        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
#        return Response(serializer.data)

#    def post(self, request, format=None):
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#class SnippetDetail(APIView):

#    def get_object(self, pk):
#        return get_object_or_404(klass=Snippet, pk=pk)

#    def get(self, request, pk, format=None):
#        serializer = SnippetSerializer(instance=self.get_object(pk))
#        return Response(serializer.data, status=status.HTTP_200_OK)

#    def put(self, request, pk, format=None):
#        serializer = SnippetSerializer(instance=self.get_object(pk), data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
#        obj = self.get_object(pk)
#        obj.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

#@api_view(http_method_names=['GET', 'POST'])
#def snippet_list(request, format=None):
#    if request.method == 'GET':
#        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
#        return Response(data=serializer.data, status=status.HTTP_200_OK)
#    elif request.method == 'POST':
#        serializer = SnippetSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@api_view(http_method_names=['GET', 'DELETE', 'PUT'])
#def snippet_detail(request, pk, format=None):
#    print(pk)
#    snippet = get_object_or_404(klass=Snippet, pk=pk)
#    if request.method == 'GET':
#        serializer = SnippetSerializer(snippet)
#        return Response(data=serializer.data)
#    elif request.method == 'PUT':
#        serializer = SnippetSerializer(instance=snippet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(data=serializer.data)
#        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == 'DELETE':
#        snippet.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
