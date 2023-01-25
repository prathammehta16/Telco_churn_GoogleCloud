from setuptools import setup
from setuptools import find_packages

REQUIRED_PACKAGES = ['xgboost==1.6.1']

setup(
    name='custom_predict',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    scripts=['predictor.py'])
