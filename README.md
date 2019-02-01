# `uninstallable`: The Uninstallable Python Wheel!

_If you got here from one of the following errors, the package you tried to
install is not intended for the platform you tried to install it on. Good day!_

```
$ pip install --user ...
...
Collecting uninstallable>0; platform_system == "..." (from ...)
  Downloading ...
Collecting pywin32>=1.0; platform_system == "Linux" (from uninstallable>0; platform_system == "..."->...)
  Could not find a version that satisfies the requirement pywin32>=1.0; platform_system == "Linux" (from uninstallable>0; platform_system == "Linux"->...) (from versions: )
No matching distribution found for pywin32>=1.0; platform_system == "Linux" (from uninstallable>0; platform_system == "Linux"->...)
```

```
$ pip install --user ...
...
Collecting uninstallable>0; platform_system != "..." (from ...)
  Could not find a version that satisfies the requirement uninstallable>0; platform_system != "..." (from ...) (from versions: )
No matching distribution found for uninstallable>0; platform_system != "..." (from ...)
```

## Why?????????

The purpose of this package is to get around a limitation of the Python Wheel
specification. It exists to prevent the successful installation of pure Python
Wheels on platforms not compatible with one's package.

## How?

PyPI doesn't allow uploading Python Wheels with unrecognized platform types, so
to force a conflict:

* We build only for the `manylinux1_x86_64` platform
* We have `setup.py` `install_requires=` a Linux-incompatible package when the
  platform is Linux

This results in either a failure to locate an applicable `uninstallable`
package file, or a realization that the package has a dependency that cannot be
installed.

## Building

```bash
python setup.py bdist_wheel -p manylinux1_x86_64
```

## Usage

```python
from setuptools import setup

setup(
  name='...',
  version='1.0.0',
  description='...',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author='...',
  author_email='...',
  url='...',
  license='...',

  python_requires='...',
  install_requires=[
    ...
    'uninstallable > 0;platform_system!="Linux"',
  ],
  ...
```

## Features

* None!
