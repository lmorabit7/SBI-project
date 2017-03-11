from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='myhmoments',
      version='0.1',
      description='Calculator of hydropathy moments in surface regions of biomolecules',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Structural bioanalysis :: Bioinformatics',
      ],
      keywords='funniest joke comedy flying circus',
      author='Claudia Arnedo, Rosa Barcelona, Laura Mora',
      author_email='labmatch@mail.com',
      license='MIT',
      packages=['myhmoments'],
      install_requires=[
          'numpy','biopython',
      ],
      entry_points={
          'console_scripts': [
              'myhmoments = myhmoments.__main__:main'
          ]
      },
      zip_safe=False)
