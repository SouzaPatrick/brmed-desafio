from rest_framework import serializers
class GraphSerializer(serializers.Serializer):
    start_date = serializers.CharField(max_length=200)
    end_date = serializers.CharField(max_length=200)
