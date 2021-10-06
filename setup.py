import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
INSTALL_REQUIRED = (HERE / "requirements.txt").read_text()
SETUP_REQUIRED = (HERE / "setup_requirements.txt").read_text()
TEST_REQUIRED = (HERE / "test_requirements.txt").read_text()

setup(
    name='weconnect-cli',
    packages=['weconnect_cli'],
    version=open("weconnect_cli/__version.py").readlines()[-1].split()[-1].strip("\"'"),
    description='Commandline Interface to interact with the Volkswagen WeConnect Services',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Till Steinbach',
    keywords='weconnect, we connect, carnet, car net, volkswagen, vw, telemetry',
    url='https://github.com/tillsteinbach/WeConnect-cli',
    project_urls={
        'Funding': 'https://github.com/sponsors/tillsteinbach',
        'Source': 'https://github.com/tillsteinbach/WeConnect-cli',
        'Bug Tracker': 'https://github.com/tillsteinbach/WeConnect-cli/issues',
    },
    license='MIT',
    install_requires=INSTALL_REQUIRED,
    entry_points={
        'console_scripts': [
            'weconnect-cli = weconnect_cli.weconnect_cli_base:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Topic :: System :: Monitoring',
    ],
    python_requires='>=3.7',
    setup_requires=SETUP_REQUIRED,
    tests_require=TEST_REQUIRED,
)
