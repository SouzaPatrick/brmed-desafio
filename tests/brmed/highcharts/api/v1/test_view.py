import pytest
from rest_framework import status


@pytest.mark.django_db
def test_highcharts_api_view(client, mocker):
    mocker.patch(
        "brmed.highcharts.api.v1.views.VatComplyRequest.main",
        return_value=[
            mocker.Mock(),
            mocker.Mock(),
            mocker.Mock(),
            mocker.Mock(),
            mocker.Mock(),
        ],
    )
    response = client.get("/highcharts/api/?start_date=2023-02-04&end_date=2023-02-08")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "BRL": [],
        "EUR": [],
        "JPY": [],
        "start_date": {"day": 4, "month": 2, "year": 2023},
        "end_date": {"day": 8, "month": 2, "year": 2023},
    }
