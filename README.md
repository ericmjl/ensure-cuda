# ensure-cuda

A small utility to ensure that one's `LD_LIBRARY_PATH` is set correctly at runtime.

Made with ❤️ by Eric J. Ma (@ericmjl).

## Usage

```bash
pip install ensure-cuda
```

Then, in a Python environment:

```python
import ensure_cuda
```

If you want to sanity-check your `LD_LIBRARY_PATH`:

```python
import os
os.getenv("LD_LIBRARY_PATH")
# or else:
assert os.getenv("CONDA_PATH") in os.getenv("LD_LIBRARY_PATH")
```

## Get started for development

To get started:

```bash
git clone git@github.com:ericmjl/ensure-cuda
cd ensure-cuda
mamba env update -f environment.yml
conda activate ensure-cuda
python -m pip install -e .
```
