"""Top-level API for ensure-cuda.

This is the file from which you can do:

    from ensure_cuda import some_function

Use it to control the top-level API of your Python data science project.
"""
import os

try:
    if os.environ["CONDA_PREFIX"] not in os.environ["LD_LIBRARY_PATH"]:
        os.environ["LD_LIBRARY_PATH"] = (
            f"{os.environ['CONDA_PREFIX']}/lib:"
            f"{os.environ['LD_LIBRARY_PATH']}"
        )
        print("Set LD_LIBRARY_PATH to include $CONDA_PREFIX")
except KeyError:
    pass
