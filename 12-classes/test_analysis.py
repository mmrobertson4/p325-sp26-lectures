import pytest

from analysis import TemperatureAnalysis

@pytest.fixture
def temperature_analysis():
    """A temperature analysis instance that will be available to all tests"""
    temperature_analysis = TemperatureAnalysis('weather_data.json', 'temperature_newyorkcity')
    return temperature_analysis


def test_average(temperature_analysis):
    """Input file is a sine wave over 3 periods, average should be close to zero"""
    assert abs(temperature_analysis.average()) < 1e-10


def test_std(temperature_analysis):
    """Input file is a sine wave with amplitude 5, standard deviation should be A/sqrt(2) = 3.5355"""
    assert abs(temperature_analysis.std() - 3.5355) < 1e-4