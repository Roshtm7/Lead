from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

class BookListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        context={"message":"listing all books"}
        return Response(data=context)

    def post(Self,request,*args,**kwargs):
        context={"message":"creating a new book object"}
        return Response(data=context)

class BookRetrieveUpdateDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        context={"message":"fetch a specific book detail"}
        return Response(data=context)

    def put(self,request,*args,**kwargs):
        context={"message":"logic for updating a book"}
        return Response(data=context)

    def delete(self,request,*args,**kwargs):
        context={"message":"logic for deleting a book"}
        return Response(data=context)