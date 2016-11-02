"""`Dependency injector` setup script."""

import os
import re

from setuptools import setup, Extension


# Defining setup variables:
defined_macros = list()
package_data = dict([('dependency_injector', ['*.pxd'])])

# Getting description:
with open('README.rst') as readme_file:
    description = readme_file.read()

# Getting requirements:
with open('requirements.txt') as version:
    requirements = version.readlines()

# Getting version:
with open('src/dependency_injector/__init__.py') as init_file:
    version = re.search('VERSION = \'(.*?)\'', init_file.read()).group(1)

# Adding debug options:
if os.environ.get('DEPENDENCY_INJECTOR_DEBUG_MODE') == '1':
    defined_macros.append(('CYTHON_TRACE', 1))
    defined_macros.append(('CYTHON_TRACE_NOGIL', 1))

    package_data['dependency_injector'].append('*.pyx')
    package_data['dependency_injector'].append('*.c')


setup(name='dependency-injector',
      version=version,
      description='Dependency injection microframework for Python',
      long_description=description,
      author='ETS Labs',
      author_email='rmogilatov@gmail.com',
      maintainer='Roman Mogilatov',
      maintainer_email='rmogilatov@gmail.com',
      url='https://github.com/ets-labs/python-dependency-injector',
      download_url='https://pypi.python.org/pypi/dependency_injector',
      install_requires=requirements,
      packages=[
          'dependency_injector',
          'dependency_injector.providers',
      ],
      package_dir={
          '': 'src',
      },
      ext_modules=[
          Extension('dependency_injector.injections',
                    ['src/dependency_injector/injections.c'],
                    define_macros=defined_macros,
                    extra_compile_args=['-O2']),
      ],
      package_data=package_data,
      zip_safe=True,
      license='BSD New',
      platforms=['any'],
      keywords=[
          'DI',
          'Dependency injection',
          'IoC',
          'Inversion of Control',
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ])
