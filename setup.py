from setuptools import setup, find_packages

setup(name='gstat',
      vesrion='0.0.1',
      author='Viliam Serecun',
      author_email='v.serecun@gmail.com',
      packages=find_packages(),
      licence="MIT",
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
      ],
      install_requires=[
          'pyshark',
      ],
      include_package_data=True,
      zip_safe=False,
      )
