from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking


class ListBooks(APIView):
    

    def get(self, request, format=None):
        bookings = [
            {
                'id': booking.id,
                'service': booking.service,
                'date': booking.date,
                'time': booking.time,
            }
            for booking in Booking.objects.filter(user=request.user)
        ]
        return Response(bookings)

    def post(self, request, format=None):

        service = request.data.get('service')
        date = request.data.get('date')
        time = request.data.get('time')


        booking = Booking.objects.create(
            user=request.user,
            service=service,
            date=date,
            time=time
        )

        return Response({
            'message': f'Запись создана',
            'id': booking.id
        })
    
