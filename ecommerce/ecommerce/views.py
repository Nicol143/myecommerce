from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    customer={'user':'Ana', 'name':'Mary','email':'ana@mary'}
    return Response(customer)