from setuptools import find_packages, setup
setup(
    name='DBSpythonlib',
    packages=find_packages(include=['DBSpythonlib']),
    version='0.0.1',
    description='Initial DBS library',
    author='Code Blasters',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)