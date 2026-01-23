from .models import Booking
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer, BookingUpdateSerializer




class ListBooking(APIView):

    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        booking = Booking.objects.create(**data)

        booking_data = BookingSerializer(booking)
        return Response(booking_data.data)


class DetailBooking(APIView):

    def get(self, request, id, format=None):
        booking = get_object_or_404(Booking, id=id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        booking = get_object_or_404(Booking, id=id)
        serializer = BookingUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        booking.service = data.get('service', booking.service)
        booking.date = data.get('date', booking.date)
        booking.time = data.get('time', booking.time)
        booking.save()

        booking_data = BookingSerializer(booking)
        return Response(booking_data.data)

    def delete(self, request, id, format=None):
        booking = get_object_or_404(Booking, id=id)
        booking.delete()
        return Response({
            "detail": f"Удалён booking с id: {id}"
        })


