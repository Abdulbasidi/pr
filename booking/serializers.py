from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)


class BookingUpdateSerializer(serializers.Serializer):
    service = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    time = serializers.TimeField(required=False)



class BookingUpdateSerializer(serializers.Serializer):
    service = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    time = serializers.TimeField(required=False)


