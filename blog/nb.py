import os
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from IPython import get_ipython
from IPython.display import Markdown, display
from matplotlib import pyplot as plt
from tqdm.notebook import tqdm

from .styling import set_blog_style

ipy = get_ipython()

# Path
Path.ls = lambda x: sorted(x.iterdir())
Path.rm = Path.unlink

# IPy Magic
ipy.magic('matplotlib inline')
ipy.magic('load_ext autoreload')
ipy.magic('autoreload 2')

# Display
set_blog_style()

np.set_printoptions(suppress=True, linewidth=120, edgeitems=8, precision=5)
pd.set_option('display.max_columns', 50)
pd.set_option('min_rows', 20)
pd.set_option('precision', 5)
pd.set_option('colheader_justify', 'left')
pd.set_option('display.multi_sparse', False)
pd.set_option('mode.chained_assignment', None)


# END


def show_imports(imports_only=False):
    s = '```python\n'
    with open(Path(__file__), 'r') as f:

        for line in f.readlines():
            if 'END' in line:
                break
            if not imports_only:
                s += line
            elif 'import ' in line:
                s += line
    s += '```'
    display(Markdown(s))


__all__ = ['os', 'sys', 'pd', 'np', 'plt', 'Path', 'joblib', 'tqdm', 'display', 'Markdown',
           'show_imports', 'set_blog_style']
