
from setuptools import setup

setup(
    name='My Application Template',
    version='0.1',
    packages=['myApp'],
    install_requires=['Flask'],
    include_package_data=True,
    zip_safe=False,
    long_description=__doc__,
)