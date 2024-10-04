## PyPI Chart Badge

This action allows you to create and put fancy-looking chart badges indicating the recent download rate of your Python packages in the README.

### Examples
This chart depicts the download rate of some popular Python packages over the last 15 days. (It dynamically updates every 24 hours)

| fastapi | django | requests | pydantic |
| ------- | ------ | -------- | ---- |
| ![](.pypi_chart/artifact/fastapi_badge.svg) | ![](.pypi_chart/artifact/django_badge.svg) | ![](.pypi_chart/artifact/requests_badge.svg) | ![](.pypi_chart/artifact/pydantic_badge.svg) |


### Basic Usage
```yml
name: Update the PyPI chart badge

on:
  schedule:
    - cron: "0 0 1 * *"  # <= runs every month

jobs:
  update-chart-badge:
    name: Updating the pypi chart badge
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Updating the badge
        uses: lnxpy/pypi-chart-badge@v1
        with:
          package_name: '<PACKAGE-NAME>'

      - uses: EndBug/add-and-commit@v9
        with:
          default_author: github_actions
          message: 'chart badge updated'

```

After each run, you'll have your badge stored in `.pypi_chart/badge.svg` of your repository.

> [!IMPORTANT]
> You have to give the "Write Access" to your workflow so that changes can be committed back into the repo.

### Options

| Option           | Default value     | Description                                                                                     | Required   |
| :--------------: | :---------------: |-------------------------------------------------------------------------------------------------|:----------:|
| `package_name`   | -                 | The Package name                                                                                    | Yes        |
| `badge_width`    | `60`              | Badge width size in pixels                                                                      | No         |
| `badge_height`   | `20`              | Badge height size in pixels                                                                     | No         |
| `badge_color`    | `'#4492F9'`       | Badge plot color (HEX or CSS color names)                                                 | No         |
| `days_limit`     | `15`              | The amount of selected days                                                                     | No         |
| `output_path`    | `.pypi_chart/`  | Badge file path directory                                                                       | No         |
| `file_name`      | `badge.svg`       | Badge file name and extension (`.png`, `.jpg`, `.jpeg`, `.webp`, and `.pdf` are also supported) | No         |

### License
MIT license terms.
