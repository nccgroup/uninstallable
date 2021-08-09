import sys

if len(sys.argv) != 4 or (
    sys.argv[1] != "bdist_wheel" or
    sys.argv[2] != "-p" or
    "linux" not in sys.argv[3]
  ):
  sys.stderr.write(b"usage: python setup.py bdist_wheel -p manylinux1_x86_64\n")
  sys.exit(1)

from setuptools import setup

setup(
  name='uninstallable',
  version='0.9.4',
  description='A purposefully uninstallable package.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author='Jeff Dileo',
  author_email='jeff.dileo@nccgroup.com',
  url='https://github.com/nccgroup/uninstallable',
  license='BSD (2 Clause)',

  install_requires=[
    'pywin32 == 301;platform_system=="Linux"',
  ],
  include_package_data=True,
  packages=['uninstallable'],

  classifiers=[
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Operating System :: OS Independent'
  ],
  keywords='uninstallable'
)
