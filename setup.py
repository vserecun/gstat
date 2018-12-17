from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='gstat',
      vesrion='0.0.1',
      description='Goose protocol script extractor',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='Goose, csv, extractor',
      url='https://github.com/vserecun/gstat',
      author='Viliam Serecun',
      author_email='iserecun@fit.vutbr.cz',
      licence="MIT",
      packages=find_packages(),
      install_requires=[
          'pyshark',
      ],
      scripts=['bin/goose_stat.py'],
      include_package_data=True,
      zip_safe=False,
      )
