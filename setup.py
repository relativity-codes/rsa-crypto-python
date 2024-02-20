from setuptools import setup, find_packages

setup(
    name='rsa-crypto',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'python-dotenv'
    ],
    test_suite='tests',
)