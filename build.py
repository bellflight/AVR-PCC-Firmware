import argparse
import os
import shutil
import subprocess

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
BUILD_DIR = os.path.join(THIS_DIR, ".pio", "build", "adafruit_feather_m4")
DIST_DIR = os.path.join(THIS_DIR, "dist")


def main(version: str) -> None:
    cmd = ["pio", "run", "--verbose"]
    subprocess.check_call(cmd, cwd=THIS_DIR)

    # clean output directory
    if os.path.isdir(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)

    # copy newly built file
    shutil.copy(
        os.path.join(BUILD_DIR, "firmware.bin"),
        os.path.join(DIST_DIR, f"pcc_firmware.{version}.bin"),
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
