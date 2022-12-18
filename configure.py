import os
import subprocess

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    queue_dir = os.path.join(THIS_DIR, "libraries", "Queue")

    # apply patch
    subprocess.check_call(
        ["git", "submodule", "update", "--init", "--recursive", queue_dir]
    )
    subprocess.check_call(["git", "reset", "--hard"], cwd=queue_dir)
    subprocess.check_call(
        [
            "git",
            "apply",
            "--ignore-whitespace",
            "--verbose",
            os.path.join(THIS_DIR, "libraries", "queue-default.patch"),
        ],
        cwd=queue_dir,
    )
    subprocess.check_call(
        [
            "git",
            "update-index",
            "--assume-unchanged",
            os.path.join("src", "cppQueue.h"),
        ],
        cwd=queue_dir,
    )

    # this needs to come after the pip install
    import platformio  # noqa

    if platformio.VERSION[0] >= 6:
        # https://docs.platformio.org/en/latest/core/userguide/pkg/cmd_install.html#cmd-pkg-install
        subprocess.check_call(["pio", "pkg", "install"], cwd=THIS_DIR)
