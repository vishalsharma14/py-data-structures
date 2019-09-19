from setuptools import setup


# Get the long description from the README.md file
with open('README.md') as description_file:
    long_description = description_file.read()


setup(
    name='py-data-structures',
    packages=['data_structures'],
    version='0.1.2',
    license='MIT',
    description='Some widely used data structures',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Vishal',
    author_email='vishal.sharma9597@gmail.com',
    url='https://github.com/vishalsharma14/py-data-structures',
    # download_url='https://github.com/vishalsharma14/py-data-structures/v_01.tar.gz',
    keywords=['DATA STRUCTURES', 'STACK', 'QUEUE'],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
    ],
)
