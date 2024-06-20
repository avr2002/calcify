from setuptools import setup, find_packages

setup(
    name="calcify",  # name of the package
    version="0.0.0",  # version of the package
    packages=find_packages(where="src"),  # where to look for our package
    package_dir={"": "src"},  # tell setuptools our package code is under src/ directory
    # package metadata
    author="Amit Vikram Raj",
    author_email="your_email@gmail.com",
    description="A simple calculator to demo Python Packaging",
    license="MIT",
)
