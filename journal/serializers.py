from .models import Entry
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Entry
        # the fields that should be included in the serialized output
        fields = ['id', 'game_title', 'date', 'entry_subject', 'entry']