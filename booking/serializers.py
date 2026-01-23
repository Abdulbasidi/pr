from rest_framework import serializers
from .models import Booking




class BookingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    time = serializers.TimeField(required=True)


class BookingUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.CharField(required=False)
    date = serializers.DateField(required=False)
    time = serializers.TimeField(required=False)






class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields ='__all__'