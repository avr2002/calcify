from setuptools import find_packages, setup

setup(
    name="calcify",  # name of the package
    version="0.0.0",  # version of the package
    packages=find_packages(where="src"),  # where to look for our package
    package_dir={"": "src"},  # tell setuptools our package code is under src/ directory
    install_requires=[
            "setuptools", # build dependency to build the source distribution
            "wheel",    # build dependency to build the binary distribution(wheel)
            "numpy",    # package dependency
        ],  # dependencies to install for our package to work
    # package metadata
    author="Amit Vikram Raj",
    author_email="your_email@gmail.com",
    description="A simple calculator to demo Python Packaging",
    license="MIT",
)
