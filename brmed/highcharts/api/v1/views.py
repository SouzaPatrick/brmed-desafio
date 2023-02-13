from datetime import date, datetime, timedelta

import requests
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from brmed.highcharts.api.v1.serializers import GraphSerializer
from brmed.highcharts.utils.convert_date_str import convert_str_to_date
from brmed.highcharts.utils.generate_renge_dates import (
    generate_renge_dates,
    generate_renge_dates_working_days,
)
from brmed.highcharts.utils.vatcomply import VatComplyRequest


class HighchartsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        start_date: str = request.GET.get("start_date", "")
        end_date: str = request.GET.get("end_date", "")
        serializer = GraphSerializer(
            data={"start_date": start_date, "end_date": end_date}
        )

        data: dict = {
            "BRL": [],
            "EUR": [],
            "JPY": [],
        }
        if serializer.is_valid():
            start_date: date = convert_str_to_date(start_date)
            end_date: date = convert_str_to_date(end_date)

        elif start_date == "" or end_date == "":
            end_date: date = datetime.now().date() - timedelta(days=1)
            start_date: date = end_date - timedelta(days=4)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        working_days: list[datetime.date] = generate_renge_dates_working_days(
            date_start=start_date, date_end=end_date
        )
        responses: list[requests.Response] = VatComplyRequest().main(
            working_days=working_days
        )

        dates_generated: list[datetime.date] = generate_renge_dates(
            date_start=start_date, date_end=end_date
        )
        # date_generated_used: list[datetime.date] = []
        count_response: int = 0
        for date_generated in dates_generated:
            if date_generated not in working_days:
                data["BRL"].append(None)
                data["EUR"].append(None)
                data["JPY"].append(None)
            else:
                if count_response <= len(responses):
                    response: requests.Response = responses[count_response]
                    if response.status_code == status.HTTP_200_OK:
                        data["BRL"].append(response.json().get("rates").get("BRL"))
                        data["EUR"].append(response.json().get("rates").get("EUR"))
                        data["JPY"].append(response.json().get("rates").get("JPY"))
                    else:
                        data["BRL"].append(None)
                        data["EUR"].append(None)
                        data["JPY"].append(None)
                    count_response += 1
                else:
                    break

        data["start_date"] = {
            "day": dates_generated[0].day,
            "month": dates_generated[0].month,
            "year": dates_generated[0].year,
        }
        data["end_date"] = {
            "day": dates_generated[-1].day,
            "month": dates_generated[-1].month,
            "year": dates_generated[-1].year,
        }

        return Response(data)
