# Peripheral Control Computer Firmware

[![Build PCC Firmware](https://github.com/bellflight/AVR-PCC-Firmware/actions/workflows/build.yml/badge.svg)](https://github.com/bellflight/AVR-PCC-Firmware/actions/workflows/build.yml)

## Setup

It's assumed you have a version of Python installed from
[python.org](https://python.org) that is the same or newer as
defined in [`.python-version`](.python-version).

First, install [Poetry](https://python-poetry.org/):

```bash
python -m pip install pipx --upgrade
pipx ensurepath
pipx install poetry
# (Optionally) Add pre-commit plugin
poetry self add poetry-pre-commit-plugin
```

Now, you can clone the repo and install dependencies:

```bash
git clone https://github.com/bellflight/AVR-PCC-Firmware
cd AVR-PCC-Firmware
poetry install --sync
poetry run pre-commit install --install-hooks
poetry run python configure.py
```

## Building

To build the firmware, run

```bash
poetry run python build.py
```

This will create a `pcc_firmware.<hash>.bin` file in `dist`.

## Flashing

Follow the instructions in the documentation, or use the upload functionality
in PlatformIO directly.
