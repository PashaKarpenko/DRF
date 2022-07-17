from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date
from rest_framework.views import APIView
from .serializers import CalculatorSerializer, StoreSerializer
from .models import Store
from rest_framework.status import HTTP_201_CREATED


@api_view(http_method_names=['GET'])
def today(request):
    today = date.today()
    return Response({'date': today, 'year': today.year, 'month': today.month, 'day': today.day })


@api_view(http_method_names=['GET'])
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
        action = serializer.data["action"]
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
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)













