from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from datetime import date
from rest_framework.views import APIView
from .serializers import CalculatorSerializer, StoreSerializer
from .models import Store
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User


@api_view(http_method_names=['GET'])
def today(request):
    today = date.today()
    date_d_m_y = date.today().strftime('%d/%m/%Y')
    return Response({'date': date_d_m_y, 'year': today.year, 'month': today.month, 'day': today.day })


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def hello_world(request):
    return_dict = {'msg': 'Hello World'}
    return Response(return_dict)


@api_view(http_method_names=['GET'])
def my_name(request):
    my_name = {'name': 'Pavel Karpenko' }
    return Response(my_name)


class CalculatorApiView(APIView):
    def post(self, request):
        serializer = CalculatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        action = serializer.data['action']
        number1 = serializer.data['number1']
        number2 = serializer.data['number2']
        if action == "minus":
            result = number1 - number2
        if action == "plus":
            result = number1 + number2
        if action == "divide":
            result = number1 / number2
        if action == "multiply":
            result = number1 * number2
        return Response({"result": result})


class StoreApiView(APIView):
    def get(self, request):
        stores = Store.objects.filter(owner__isnull=True)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)


class StoresViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MyStoreViewSet(ModelViewSet):
    user = User.objects.get()
    queryset = Store.objects.filter(owner_id=user.id).all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_deactivated(self, request, pk=None):
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class AdminStoreViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    user = User.objects.get()
    if user.is_staff == True:
        queryset = Store.objects.all()
        serializer_class = StoreSerializer
        permission_classes = [IsAuthenticated]
        filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = ['status']
        search_fields = ['name']
        ordering_fields = ['rating']

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_active(self, request, pk=None):
        store = self.get_object()
        if store.status == 'in_review':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)
