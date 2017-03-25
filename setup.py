from setuptools import setup

setup(
    name="py-nestle1904",
    version="0.1",
    description="pip-installable Nestle 1904 with Python API",
    license="MIT",
    url="https://github.com/biblicalhumanities/py-nestle1904",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    packages=["pynestle1904"],
    package_data={"": ["nestle1904.csv"]},
)
