from rest_framework import serializers


class GraphSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, data):
        if data.get('start_date') > data.get('end_date'):
            raise serializers.ValidationError("The value entered for the date range is invalid")
        return data
