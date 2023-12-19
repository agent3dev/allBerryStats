import json
from dotenv import load_dotenv
import os
from icecream import ic
import requests
import requests_cache
import numpy as np

load_dotenv()
requests_cache.install_cache(expire_after=os.getenv("EXPIRATION"),
                             allowable_methods='GET')

class BerryStats:
    def __init__(self):
        self.base_addr = os.getenv("ROOT_URL")
        self.berries_names, self.growth_times = self.fetch_berries()

    def fetch_berries(self):
        main_info = self.fetch_data(self.base_addr)
        berries_info = [self.fetch_data(self.base_addr + str(i)) for i in range(1, main_info['count'] + 1)]
        berries = [berry['name'] for berry in berries_info]
        growth_times = [berry['growth_time'] for berry in berries_info]
        return berries, growth_times

    def get_stats(self):
        min_growth_time = int(np.min(self.growth_times))
        median_growth_time = int(np.median(self.growth_times))
        max_growth_time = int(np.max(self.growth_times))
        variance_growth_time = np.var(self.growth_times).round(2)
        mean_growth_time = np.mean(self.growth_times).round(2)
        unique, counts = np.unique(self.growth_times, return_counts=True)
        frequency_growth_time = {int(unique[i]): int(count) for i, count in enumerate(counts)}
        result = {
            "berries_names": self.berries_names,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": frequency_growth_time
            }
        return json.dumps(result)

    @staticmethod
    def fetch_data(url, show_hits=False):
        session = requests.Session()
        if show_hits:
            if session.cache.contains(url=url):
                print(f'Cache hit for URL: {url}')
            else:
                print(f'Cache miss for URL: {url}')
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f'An error occurred while fetching data from {url}: {response.status_code}')
        except requests.exceptions.BaseHTTPError as e:
            raise Exception(f'An error occurred while fetching data from {url}: {e}')
