# Nitpick

[![PyPI](https://img.shields.io/pypi/v/nitpick.svg)](https://pypi.org/project/nitpick)
![GitHub Actions Python Workflow](https://github.com/andreoliwa/nitpick/workflows/Python/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/nitpick/badge/?version=latest)](https://nitpick.rtfd.io/en/latest/?badge=latest)
[![Coveralls](https://coveralls.io/repos/github/andreoliwa/nitpick/badge.svg)](https://coveralls.io/github/andreoliwa/nitpick)
[![Maintainability](https://api.codeclimate.com/v1/badges/61e0cdc48e24e76a0460/maintainability)](https://codeclimate.com/github/andreoliwa/nitpick)
[![Test Coverage](https://api.codeclimate.com/v1/badges/61e0cdc48e24e76a0460/test_coverage)](https://codeclimate.com/github/andreoliwa/nitpick)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/nitpick.svg)](https://pypi.org/project/nitpick/)
[![Project License](https://img.shields.io/pypi/l/nitpick.svg)](https://pypi.org/project/nitpick/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=andreoliwa/nitpick)](https://dependabot.com)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/andreoliwa/nitpick/develop.svg)](https://results.pre-commit.ci/latest/github/andreoliwa/nitpick/develop)

Command-line tool and `flake8` plugin to enforce the same settings across multiple language-independent projects.

Useful if you maintain multiple projects and are tired of copying/pasting the same INI/TOML/YAML/JSON keys and values over and over, in all of them.

The tool now has an "apply" feature that modifies configuration files directly (pretty much like `black` and `isort` do with Python files).
See the [CLI docs for more info](https://nitpick.readthedocs.io/en/latest/cli.html).

Many more features are planned for the future, check [the roadmap](https://github.com/andreoliwa/nitpick/projects/1).

## Style file

A "nitpick code style" is a [TOML](https://github.com/toml-lang/toml) file with the settings that should be present in config files from other tools.

Example of a style:

```
["pyproject.toml".tool.black]
line-length = 120

["pyproject.toml".tool.poetry.dev-dependencies]
pylint = "*"

["setup.cfg".flake8]
ignore = "D107,D202,D203,D401"
max-line-length = 120
inline-quotes = "double"

["setup.cfg".isort]
line_length = 120
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
combine_as_imports = true
```

This style will assert that:

- ... [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort) and [flake8](https://gitlab.com/pycqa/flake8) have a line length of 120;
- ... [flake8](https://gitlab.com/pycqa/flake8) and [isort](https://github.com/PyCQA/isort) are configured as above in `setup.cfg`;
- ... [Pylint](https://www.pylint.org) is present as a [Poetry](https://github.com/python-poetry/poetry) dev dependency in `pyproject.toml`).

## Quick setup

To try the package, simply install it (in a virtualenv or globally) and run `flake8` on a project with at least one Python (`.py`) file:

    # Install with pip:
    pip install -U nitpick

    # Add to your project with Poetry:
    poetry add --dev nitpick

    # On macOS, install with Homebrew:
    brew install andreoliwa/formulae/nitpick

    # Run nitpick directly to modify your files
    nitpick run

    # Or run with flake8 to only check for errors
    flake8 .

Nitpick will download and use the opinionated [default style file](https://raw.githubusercontent.com/andreoliwa/nitpick/v0.26.0/nitpick-style.toml).

You can use it as a template to configure your own style.

### Run as a pre-commit hook (recommended)

If you use [pre-commit](https://pre-commit.com/) on your project (you should), add this to the `.pre-commit-config.yaml` in your repository:

    repos:
      - repo: https://github.com/andreoliwa/nitpick
        rev: v0.26.0
        hooks:
          - id: nitpick

To install the `pre-commit` and `commit-msg` Git hooks:

    pre-commit install --install-hooks
    pre-commit install -t commit-msg

To start checking all your code against the default rules:

    pre-commit run --all-files

---

For more details on styles and which configuration files are currently supported, [see the full documentation](https://nitpick.rtfd.io/).
