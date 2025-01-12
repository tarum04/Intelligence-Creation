from rest_framework import serializers
from .models import Record, RecordDetail

class RecordDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordDetail
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    recorddetail_set = RecordDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Record
        fields = ['id', 'masalah', 'label', 'features', 'kategori', 'status', 'recorddetail_set']

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(RecordSerializer, self).__init__(*args, **kwargs)

        # Get the 'fields' parameter from the context if available
        fields = self.context.get('fields', None)
        if fields:
            # Drop any fields that are not specified in the 'fields' parameter
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)