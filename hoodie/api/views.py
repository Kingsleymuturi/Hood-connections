from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authtoken.models import Token
from hoodie.api.serializers import RegistrationSerializer,HoodSerializer,ProfileSerializer
from hoodie.models import NeighbourHood,Profile
from rest_framework.permissions import  IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication

class HoodListView(ListAPIView):
    queryset = NeighbourHood.objects.all()
    serializer_class = HoodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def update_profile(request,pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if profile != user:
        return Response({'response': "You don't have permission to edit "})

    if request.method == "PUT":
        serializer = ProfileSerializer(profile,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
@permission_classes([IsAuthenticated])
def update_hood(request,pk):
    try:
        hood = NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if hood.admin != user:
        return Response({'response': "You don't have permission to edit "})

    if request.method == "PUT":
        serializer = HoodSerializer(hood,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def delete_hood(request,pk):
    try:
        hood = NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if hood.admin != user:
        return Response({'response': "You don't have permission to delete that "})
    
    if request.method == "DELETE":
        operation = hood.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['fail'] = 'failed to delete'
        return Response(data=data)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_hood(request):
    account = request.user
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