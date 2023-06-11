from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=["get"])
    def registered_events(self):
        queryset = Event.objects.filter(ticket__user=self.request.user).order_by(
            "start_date"
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post"]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
