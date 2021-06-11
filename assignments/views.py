from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import assignmentSerializer
from .models import Assignment
from rest_framework.exceptions import APIException


# Create your views here.

# create_assignment function gets the request with data = {"name":"Social","title":"Panipat","description":"This assignment is from chapter 1 and 5","type":"Multiple choice","duration":"02:00:00","tags":["Social","Multiple"]}
# and validates the data and stores in the Assignment model
@api_view(['POST'])
def create_assignment(request):
    response = Response()
    try:
        serializer = assignmentSerializer(data=request.data)
    except:
         return Response(
                {"error": "There was a problem in request data"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    if serializer.is_valid():
        try:
            serializer.save()
        except:
            raise APIException("There was a problem in storing the data")
    else:
        raise APIException("Post data serialization is not valid")
    response.data = {
        'message': 'success'
    }
    return response

#get_assignment function gets the primary key and searches the assignments based on primary key and if assignment is present it passes the assignment object to serializer else (not present) it raises 404 error.
@api_view(['GET'])
def get_assignment(request,pk):
    try:
        assignment = Assignment.objects.get(id=pk)
    except Assignment.DoesNotExist:
        return Response(
                {"error": "Data Not found"}, 
                status=status.HTTP_404_NOT_FOUND)
    try:
        serializer = assignmentSerializer(assignment)
    except:
        raise APIException("Error while serializing data")

    return Response(serializer.data)

# search_assignments function takes a tag as string input and returns the assignments data with that tag if that tag is not present then it will raise not found error
@api_view(['GET'])
def search_assignments(request, tag):
    try:
        queryset = Assignment.objects.filter(tags__icontains=tag)
    except:
        return Response(
                {"error": "Data Not Found"}, 
                status=status.HTTP_404_NOT_FOUND)
    try:
        serializer = assignmentSerializer(queryset, many=True)
    except:
        raise APIException("Error while serializing data")

    return Response(serializer.data)

    


