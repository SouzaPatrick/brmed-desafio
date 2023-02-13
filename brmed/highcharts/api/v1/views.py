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
    generate_renge_dates_working_days,
)
from brmed.highcharts.utils.vatcomply import VatComplyRequest


class HighchartsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        start_date: str = request.GET.get("start_date", None)
        end_date: str = request.GET.get("end_date", None)
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

        dates_generated: list[datetime.date] = generate_renge_dates_working_days(
            date_start=start_date, date_end=end_date
        )
        responses: list[requests.Response] = VatComplyRequest().main(
            dates_generated=dates_generated
        )

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

        for response in responses:
            if response.status_code == status.HTTP_200_OK:
                data["BRL"].append(response.json().get("rates").get("BRL"))
                data["EUR"].append(response.json().get("rates").get("EUR"))
                data["JPY"].append(response.json().get("rates").get("JPY"))
        # data: dict = {
        #     "BRL": [
        #         5.066654475633173,
        #         5.066654475633173,
        #         5.161933927245732,
        #         5.160373831775701,
        #         5.183418723800653,
        #         5.214464766502647,
        #     ],
        #     "EUR": [
        #         0.9143275121148396,
        #         0.9143275121148396,
        #         0.9279881217520417,
        #         0.9345794392523364,
        #         0.9315323707498836,
        #         0.9284189026088572,
        #     ],
        #     "JPY": [
        #         128.41729907652922,
        #         128.41729907652922,
        #         132.15478841870825,
        #         132.05607476635515,
        #         131.1690731252911,
        #         130.7213814873271,
        #     ],
        # }
        # end_date: date = datetime.now().date() - timedelta(days=1)
        # start_date: date = end_date - timedelta(days=5)
        # data["start_date"] = {
        #     "day": start_date.day,
        #     "month": start_date.month,
        #     "year": start_date.year,
        # }
        # data["end_date"] = {
        #     "day": end_date.day,
        #     "month": end_date.month,
        #     "year": end_date.year,
        # }
        return Response(data)
