import os
import sys
from setuptools import setup
from setuptools.command.test import test


test_args = [
    '--verbose',
    '--capture=sys',
    '--log-level=INFO',
    '--log-file-level=INFO',
    '--cov-report=html',
    '--cov-report=term',
    '--cov=mnist',
    'test',
]


class PyTest(test):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        os.environ['ENV'] = 'test'
        test.initialize_options(self)
        self.pytest_args = test_args

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='mnist',
    version='0.0.0',
    description='Simple MNIST classifier example using PyTorch Lightning.',
    long_description='https://github.com/kengz/mnist-classifier',
    keywords='mnist',
    url='https://github.com/kengz/mnist-classifier',
    author='kengz',
    author_email='kengzwl@gmail.com',
    packages=['mnist'],
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    dependency_links=[],
    extras_require={
        'dev': [],
        'docs': [],
        'testing': [],
    },
    classifiers=[],
    test_suite='test',
    cmdclass={'test': PyTest},
)
