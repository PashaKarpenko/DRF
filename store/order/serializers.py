from rest_framework import serializers
from .models import Store


class TestSerializer(serializers.Serializer):
    text = serializers.CharField()
    number = serializers.IntegerField()


class CalculatorSerializer(serializers.Serializer):
    action = serializers.CharField()
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

    def validate(self, data):
        if data["action"] not in ["minus", "plus", "divide", "multiply"]:
            raise serializers.ValidationError("action може бути тільки з наданого списку: 'minus', 'plus', 'divide', 'multiply'")
        if data["action"] == "divide" and data["number2"] == 0:
            raise serializers.ValidationError("Ділення на 0 неможливе")
        return data


class OrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=100)

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store