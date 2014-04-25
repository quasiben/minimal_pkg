
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'minimal_pkg',
    description='Minimal Example Package',
    author = 'Benjamin Zaitlen',
    version= '0.1',
    packages = ['minimal_pkg'],
)
