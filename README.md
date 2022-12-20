# Peripheral Control Computer Firmware

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

This will create a `pcc_firmware.<hash>.bin` file in `PCC/.pio/build/adafruit_feather_m4`.

## Flashing

Follow the instructions in the documentation, or use the upload functionality
in PlatformIO directly.
