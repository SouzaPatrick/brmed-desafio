from datetime import date

import pytest

from brmed.highcharts.api.v1.serializers import GraphSerializer
from brmed.highcharts.utils.serializer_error_detail import extract_error_detail


@pytest.mark.parametrize(
    "date_range",
    [
        {"start_date": "2023-02-04", "end_date": "2023-02-08"},
        {"start_date": date(2023, 2, 4), "end_date": date(2023, 2, 8)},
    ],
)
def test_input_data_type_graph_serializer(date_range):
    serializer = GraphSerializer(data=date_range)

    assert serializer.is_valid() is True
    assert serializer.data == {"start_date": "2023-02-04", "end_date": "2023-02-08"}

def test_input_data_type_graph_serializer_invalid():
    serializer = GraphSerializer(data={"start_date": "2023-02-08", "end_date": "2023-02-04"})

    assert serializer.is_valid() is False
    assert extract_error_detail(serializer.errors)[0]["error_message"] == "The value entered for the date range is invalid"
