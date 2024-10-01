## PyPI Chart Badge <img alt="action-badge" src="https://img.shields.io/badge/pypi chart badge-white?logo=github-actions&label=GitHub%20Action&labelColor=white&color=0064D7"> <a href="https://github.com/lnxpy/pyaction"><img alt="pyaction" src="https://img.shields.io/badge/PyAction-white?label=Made%20with&labelColor=white&color=0064D7"></a>

This action allows you to create and put fancy-looking chart badges indicating the recent download rate of your Python packages in the README.

Examples: ![chart_1](examples/chart_1.svg) ![chart_2](examples/chart_2.svg) ![chart_3](examples/chart_3.svg) ![chart_4](examples/chart_4.svg) ![chart_5](examples/chart_5.svg)


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

### More Options

| Option           | Default value     | Description                                                                                     | Required   |
| :--------------: | :---------------: |-------------------------------------------------------------------------------------------------|:----------:|
| `package_name`   | -                 | Package name                                                                                    | Yes        |
| `badge_width`    | `60`              | Badge width size in pixels                                                                      | No         |
| `badge_height`   | `20`              | Badge height size in pixels                                                                     | No         |
| `badge_color`    | `'#4492F9'`       | Badge plot color (HEX or CSS-valid color names)                                                 | No         |
| `days_limit`     | `15`              | The amount of selected days                                                                     | No         |
| `output_path`    | `.pypi_chart/`  | Badge file path directory                                                                       | No         |
| `file_name`      | `badge.svg`       | Badge file name and extension (`.png`, `.jpg`, `.jpeg`, `.webp`, and `.pdf` are also supported) | No         |

### Licesne
MIT License terms.