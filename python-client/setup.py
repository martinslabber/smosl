# SMOSL Setup.py

from setuptools import setup, find_packages

setup(name='smosl',
      version='0.1',
      description='System Monitoring Over SysLog',
      author='martinslabber',
      url='https://github.com/martinslabber/smosl',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python"],
      platforms=["OS Independent"],
      scripts=["smosl_send"],
      packages=find_packages())
