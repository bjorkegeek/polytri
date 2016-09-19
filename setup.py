import setuptools
from polytri.version import Version


setuptools.setup(name='polytri',
                 version=Version('1.0.0').number,
                 description='Polygon triangulation algorithm',
                 long_description=open('README.md').read().strip(),
                 author='David Bj\xf6rkevik',
                 author_email='david@bjorkevik.se',
                 url='http://path-to-my-polytri',
                 py_modules=['polytri'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='polygon triangulation',
                 classifiers=['Development Status :: 4 - Beta',
                              'Topic :: Scientific/Engineering :: Mathematics'
                 ])
