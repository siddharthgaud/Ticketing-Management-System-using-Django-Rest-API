from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'priority', 'status', 'created_by', 'assigned_to', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
