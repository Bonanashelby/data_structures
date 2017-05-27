"""Create a Python distribution package setup.py."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}


setup(
    name="dll",
    description="Implements the data structure assignment",
    version=0.1,
    author="Kurt Maurer" "Anna Shelby",
    author_email="bonanashelby@gmail.com",
    license="MIT",
    py_modules=["server, client"],
    package_dir={'': 'src'},
    install_requires=["ipython", "pytest"],
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
        ]
    }
)
