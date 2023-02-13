from datetime import date

from django.conf import settings
from rest_framework import serializers
from workadays import workdays as wd


class GraphSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, data):
        start_date: date = data.get("start_date")
        end_date: date = data.get("end_date")
        # Validate if the range is valid
        if start_date > end_date:
            raise serializers.ValidationError(
                "The value entered for the date range is invalid"
            )

        # Validate if it exceeds the maximum day limit for consultation
        MAX_DAYS: int = 5
        if (
            wd.networkdays(start_date, end_date, country=settings.COUNTRY_WORKADAYS)
            > MAX_DAYS
        ):
            raise serializers.ValidationError(
                "Invalid informed period, inform a maximum range of 5 working days"
            )
        return data

    def create(self, validated_data):

        return
