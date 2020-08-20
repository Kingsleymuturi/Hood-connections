from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from hoodie.api.serializers import RegistrationSerializer,HoodSerializer
from hoodie.models import NeighbourHood,Profile


@api_view(['GET',])
def hoods(request):
    hoods = NeighbourHood.objects.all()
    serializer = HoodSerializer(hoods, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def view_hood(request,pk):
    try:
        hood = NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HoodSerializer(hood)
        return Response(serializer.data)

@api_view(['PUT',])
def update_hood(request,pk):
    try:
        hood = NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = HoodSerializer(hood,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE',])
def delete_hood(request,pk):
    try:
        hood = NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = hood.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['fail'] = 'failed to delete'
        return Response(data=data)

@api_view(['POST',])
def create_hood(request):
    account = Profile.objects.get(pk=3)

    hood = NeighbourHood(admin=account)

    if request.method == 'POST':
        serializer = HoodSerializer(hood, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)