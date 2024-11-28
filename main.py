import os
from pathlib import Path

from pyaction import PyAction
from pyaction.workflow import annotations as A

from chart import Badge
from pypi import PyPI

workflow = PyAction()


def get_or_create_path(path: str) -> str:
    """gets or creates the path then returns it

    Args:
        path (str): path

    Returns:
        str: path
    """

    if not os.path.exists(path):
        A.warning(f"Couldn't find `{path}` path in the repo. Creating it!")
        os.makedirs(path)

    return path


@workflow.action
def action(
    package_name: str,
    badge_width: int,
    badge_height: int,
    badge_color: str,
    badge_dark_color: str,
    days_limit: int,
    output_path: str,
    file_name: str,
) -> None:
    package = PyPI(package_name)
    rates_df = package.get_rates(days_limit)

    badge = Badge(rates_df).create(badge_height, badge_width, badge_color)
    dark_badge = Badge(rates_df).create(badge_height, badge_width, badge_dark_color)

    badge_path = Path(get_or_create_path(output_path)).joinpath(file_name)
    dark_badge_path = Path(get_or_create_path(output_path)).joinpath(
        f"dark_{file_name}"
    )

    badge.write_image(badge_path)
    dark_badge.write_image(dark_badge_path)
