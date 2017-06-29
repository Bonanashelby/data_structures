"""Create a Python distribution package setup.py."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest-cov', 'tox']
}


setup(
    name="Data Structures",
    description="Implements the data structure assignment",
    version=0.1,
    author="Kurt Maurer" "Anna Shelby",
    author_email="bonanashelby@gmail.com",
    license="MIT",
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages
)
