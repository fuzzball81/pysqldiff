from setuptools import setup

setup(name='pysqldiff',
      version='0.1',
      description='A python based SQL diff tool using SQLAlchemy',
      url='http://github.com/fuzzball81/pysqldiff',
      author='Jason Joyce',
      author_email='fuzzball81@gmail.com',
      license='MIT',
      packages=['pysqldiff'],
      install_requires=[
          'SQLAlchemy',
      ],
      zip_safe=False)
