from datetime import date

from brmed.highcharts.utils.convert_date_str import (
    convert_date_to_str,
    convert_str_to_date,
)


def test_convert_date_to_str():
    assert "2023-02-12" == convert_date_to_str(date(2023, 2, 12))


def test_convert_str_to_date():
    assert date(2023, 2, 12) == convert_str_to_date("2023-02-12")
