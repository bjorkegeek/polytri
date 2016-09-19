import setuptools

setuptools.setup(name='polytri',
                 version='1.0.3',
                 description='Polygon triangulation algorithm',
                 long_description=open('README.md').read().strip(),
                 author='David Bj\xf6rkevik',
                 author_email='david@bjorkevik.se',
                 url='https://github.com/bjorkegeek/polytri',
                 py_modules=['polytri'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='polygon triangulation',
                 classifiers=['Development Status :: 4 - Beta',
                              'Topic :: Scientific/Engineering :: Mathematics'
                 ])
