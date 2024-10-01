import os

from pyaction import PyAction

from chart import Badge
from pypi import Rate

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
    stats = Rate(package_name)
    rates_df = stats.get_rates(days_limit)

    badge = Badge(rates_df).create_chart(badge_height, badge_width, badge_color)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    badge.write_image(output_path + file_name,)
