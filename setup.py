from setuptools import setup


setup(
    name='check_requests',
    version='0.0',
    packages=['check_requests'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'check_requests = check_requests.cli:cli'
        ]
    }
)
