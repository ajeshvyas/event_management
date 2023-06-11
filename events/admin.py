from django.contrib import admin

from .models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "start_date", "event_type")
    list_filter = ("start_date", "event_type")


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "user", "booked_at")
    list_filter = ("event", "user")


admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
