from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer,PersonModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

import io 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin


def changed_singleobj(request,id):
    data=Person.objects.get(id=id)
    serializer=PersonModelSerializer(data)
    # print(serializer.data)

    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return Response(serializer.data)

# @csrf_exempt
@api_view(['GET','PUT','PATCH'])
def singleobj(request,id):
    data=get_object_or_404(Person,id=id)
    if request.method == 'PUT':
            # stream=io.BytesIO(request.body)
            # parsed_data=JSONParser().parse(stream)
        parsed_data=request.data
        serializer=PersonModelSerializer(data,data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':'success'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PATCH":
        parsed_data=request.data
        serializer=PersonModelSerializer(data,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':'success'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer=PersonModelSerializer(data)
        return Response(serializer.data)

# @csrf_exempt
@api_view(['GET','POST'])
def multiobj(request):
    if request.method == 'POST':
        parsed_data=request.data
        serializer=PersonModelSerializer(data=parsed_data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response({"created":"successfull"},status=status.HTTP_201_CREATED)
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created":"successfull"},status=status.HTTP_201_CREATED)



    if request.method == 'GET':
        data=Person.objects.all()
        serializer=PersonModelSerializer(data,many=True)
        # print(serializer.data)

        # json_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
        return Response(serializer.data)


class changed_SingleObjAPIView(APIView):
    def get(self,request,id):
        data=get_object_or_404(Person,id=id)
        serializer=PersonModelSerializer(data)
        return Response(serializer.data)

    def put(self,request,id):
        data=get_object_or_404(Person,id=id)
        parsed_data=request.data
        serializer=PersonModelSerializer(data,data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':'success'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        data=get_object_or_404(Person,id=id)
        parsed_data=request.data
        serializer=PersonModelSerializer(data,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'update':'success'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class changed_MultiObjAPIView(APIView):

    def get(self,request):
        data=Person.objects.all()
        serializer=PersonModelSerializer(data,many=True)
        return Response(serializer.data)


    def post(self,request):
        parsed_data=request.data
        serializer=PersonModelSerializer(data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"created":"successfull"},status=status.HTTP_201_CREATED)
    

# class SingleObjAPIView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
class SingleObjAPIView(RetrieveUpdateDestroyAPIView):

    queryset=Person.objects.all()
    serializer_class=PersonModelSerializer

        # def get(self,request,*args,**kwargs):
        #     return self.retrieve(request,*args, **kwargs)
        
        # def put(self,request,*args, **kwargs):
        #     return self.update(request,*args, **kwargs)
        
        # def patch(self,request,*args, **kwargs):
        #     return self.partial_update(request,*args, **kwargs)
        
        # def delete(self,request,*args, **kwargs):
        #     return self.destroy(request,*args, **kwargs)

# class MultiObjAPIView(CreateModelMixin,ListModelMixin,GenericAPIView):
class MultiObjAPIView(ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonModelSerializer

        # def get(self,request,*args,**kwargs):
        #     return self.list(request,*args, **kwargs)
        
        # def post(self,request):
        #     return self.create(request)
