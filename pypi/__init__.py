import requests
from pandas import DataFrame


class Rate:
    def __init__(self, package_name: str) -> None:
        self.package_name = package_name

    def get_rates(self, limit: int) -> DataFrame:
        endpoint = f"https://pypistats.org/api/packages/{self.package_name}/overall"
        r = requests.get(endpoint, params={"mirrors": True}).json()["data"][-limit:]

        return DataFrame([i["downloads"] for i in r])
