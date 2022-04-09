from setuptools import setup, find_packages

setup(
    name='mfa-aws',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=['tabulate'],
    entry_points="""
        [console_scripts]
        mfa-aws=utils:main
    """
)