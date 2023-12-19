import pytest
import json
from berries import BerryStats

@pytest.fixture
def mock_fetch_data(monkeypatch):
    def mock_fetch_data(self, url, show_hits=False):
        if url == 'https://pokeapi.co/api/v2/berry/':
            return {
                'count': 2,
                'results': [
                    {'name': 'berry1', 'growth_time': 10},
                    {'name': 'berry2', 'growth_time': 20}
                ]
            }
        elif url == 'https://pokeapi.co/api/v2/berry/1':
            return {'name': 'berry1', 'growth_time': 10}
        elif url == 'https://pokeapi.co/api/v2/berry/2':
            return {'name': 'berry2', 'growth_time': 20}
        else:
            return None

    monkeypatch.setattr(BerryStats, 'fetch_data', mock_fetch_data)

def test_fetch_berries(mock_fetch_data):
    berry_stats = BerryStats()
    berries, growth_times = berry_stats.fetch_berries()

    assert berries == ['berry1', 'berry2']
    assert growth_times == [10, 20]

def test_fetch_stats(mock_fetch_data):
    berry_stats = BerryStats()
    stats = berry_stats.get_stats()

    expected_stats = {
        "berries_names": ['berry1', 'berry2'],
        "min_growth_time": 10,
        "median_growth_time": 15,
        "max_growth_time": 20,
        "variance_growth_time": 25.0,
        "mean_growth_time": 15.0,
        "frequency_growth_time": {10: 1, 20: 1}
    }
    assert stats == json.dumps(expected_stats)
