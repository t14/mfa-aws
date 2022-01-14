from setuptools import setup, find_packages

setup(
    name='aws-tools',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=['configparser'],
    entry_points="""
        [console_scripts]
        aws-tools=utils:main
    """
)