import os

from pyaction import PyAction
from pyaction.workflow import annotations

from chart import Badge
from pypi import API

workflow = PyAction()


@workflow.action()
def action(
    package_name: str,
    badge_width: int,
    badge_height: int,
    badge_color: str,
    days_limit: int,
    output_path: str,
    file_name: str,
) -> None:
    stats = API(package_name)
    rates_df = stats.get_rates(days_limit)

    badge = Badge(rates_df).create(badge_height, badge_width, badge_color)

    if not os.path.exists(output_path):
        annotations.warning(
            f"Couldn't find `{output_path}` path in the repo. So I'm making it!"
        )
        os.makedirs(output_path)

    badge.write_image(
        output_path + file_name,
    )
