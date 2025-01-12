from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ReceivedDataSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import ReceivedData
from django.http import Http404


class CustomObtainAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         token, created = Token.objects.get_or_create(user=request.user)
    #         return Response({
    #             'token': token.key,
    #             'user_id': request.user.pk,
    #             'email': request.user.email
    #         })
    #     else:
    #         return Response({
    #             "detail": "Authentication credentials were not provided."
    #         }, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ReceiveDataAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReceivedDataSerializer
    queryset = ReceivedData.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return ReceivedData.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # Get the object with the specified primary key (pk)
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.filter(**filter_kwargs).first()
        if obj is None:
            raise Http404("No ReceivedData matches the given query.")
        return obj
    
    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj = queryset.first()
        if obj:
            # Update existing object
            serializer = self.get_serializer(obj, data=request.data)
        else:
            # Create new object
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED if not obj else status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)