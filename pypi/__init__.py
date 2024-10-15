import requests
from pandas import DataFrame
from pyaction.workflow import annotations


class PyPI:
    def __init__(self, package_name: str) -> None:
        """pypi interface

        Args:
            package_name (str): package name
        """

        self.package_name = package_name

    def get_rates(self, limit: int) -> DataFrame:
        """get the download rates

        Args:
            limit (int): days limit

        Returns:
            DataFrame: pandas vector data frame
        """

        endpoint = f"https://pypistats.org/api/packages/{self.package_name}/overall"

        r = requests.get(endpoint, params={"mirrors": True})

        if r.status_code != 200:
            annotations.error(
                f"There was an issue with fetching the package data: {r.reason}"
            )
            raise SystemExit

        return DataFrame([i["downloads"] for i in r.json()["data"][-limit:]])
