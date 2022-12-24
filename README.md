# Peripheral Control Computer Firmware

[![Build PCC Firmware](https://github.com/bellflight/AVR-PCC-Firmware/actions/workflows/build.yml/badge.svg)](https://github.com/bellflight/AVR-PCC-Firmware/actions/workflows/build.yml)

## Setup

Run

```bash
poetry install
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
