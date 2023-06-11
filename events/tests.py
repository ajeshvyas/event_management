import random

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer


class EventTests(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def generate_event_data(self):
        event_data = {
            "title": self.fake.word(),
            "description": self.fake.paragraph(),
            "start_date": timezone.make_aware(self.fake.future_datetime()),
            "end_date": timezone.make_aware(self.fake.future_datetime()),
            "max_seats": random.randint(50, 200),
            "booking_start_date": timezone.make_aware(self.fake.past_datetime()),
            "booking_end_date": timezone.make_aware(self.fake.future_datetime()),
            "event_type": random.choice(["online", "offline"]),
        }
        return event_data

    def test_list_events(self):
        num_events = random.randint(5, 10)
        for _ in range(num_events):
            Event.objects.create(**self.generate_event_data())

        url = reverse("event-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.count(), len(response.data))

    def test_retrieve_event(self):
        event_data = self.generate_event_data()
        event = Event.objects.create(**event_data)
        url = reverse("event-detail", args=[event.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EventSerializer(event)
        self.assertEqual(response.data, serializer.data)


class TicketTests(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def generate_event_data(self):
        event_data = {
            "title": self.fake.word(),
            "description": self.fake.paragraph(),
            "start_date": timezone.make_aware(self.fake.future_datetime()),
            "end_date": timezone.make_aware(self.fake.future_datetime()),
            "max_seats": random.randint(50, 200),
            "booking_start_date": timezone.make_aware(self.fake.past_datetime()),
            "booking_end_date": timezone.make_aware(self.fake.future_datetime()),
            "event_type": random.choice(["online", "offline"]),
        }
        return event_data

    def generate_ticket_data(self):
        ticket_data = {"event": Event.objects.first().id}
        return ticket_data

    def test_create_ticket(self):
        Event.objects.create(**self.generate_event_data())
        ticket_data = self.generate_ticket_data()
        url = reverse("ticket-list")
        response = self.client.post(url, ticket_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        ticket = Ticket.objects.get()
        serializer = TicketSerializer(ticket)
        self.assertEqual(response.data, serializer.data)

    def test_list_tickets(self):
        event = Event.objects.create(**self.generate_event_data())
        num_tickets = random.randint(5, 10)
        for _ in range(num_tickets):
            Ticket.objects.create(user=self.user, event=event)

        url = reverse("ticket-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Ticket.objects.count(), len(response.data))

    def test_retrieve_ticket(self):
        event = Event.objects.create(**self.generate_event_data())
        ticket = Ticket.objects.create(user=self.user, event=event)
        url = reverse("ticket-detail", args=[ticket.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TicketSerializer(ticket)
        self.assertEqual(response.data, serializer.data)
