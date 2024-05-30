"""Tests for ensure-cuda."""
import os


def test_ensure_cuda():
    """Tests that ensure-cuda behaves as expected.

    The expected behavior is that ensure-cuda
    will add the conda-prefix's `/lib` directory to the LD_LIBRARY_PATH.
    """
    os.environ["LD_LIBRARY_PATH"] = ""

    import ensure_cuda # noqa: F401, I001


    if (
        os.getenv("CONDA_PREFIX", None) is not None
        and
        os.getenv("LD_LIBRARY_PATH", None) is not None
    ):
        assert os.environ["CONDA_PREFIX"] in os.environ["LD_LIBRARY_PATH"]
