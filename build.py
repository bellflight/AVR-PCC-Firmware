import argparse
import os
import subprocess

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
BUILD_DIR = os.path.join(THIS_DIR, ".pio", "build", "adafruit_feather_m4")


def main(version: str) -> None:
    cmd = ["pio", "run", "--verbose"]

    print(cmd)
    subprocess.check_call(cmd, cwd=THIS_DIR)

    target = os.path.join(
        BUILD_DIR,
        f"pcc_firmware.{version}.bin",
    )
    if os.path.isfile(target):
        print(f"{target} already exists, replacing")
        os.remove(target)

    os.rename(
        os.path.join(BUILD_DIR, "firmware.bin"),
        target,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        default=subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip(),
    )
    args = parser.parse_args()

    main(args.version)
