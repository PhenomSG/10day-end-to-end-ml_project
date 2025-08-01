'''
It is a module used to build and distribute Python packages
'''

from setuptools import find_packages,setup

setup(

    name='ml-proj',
    version='0.0.1',
    author='phenomsg',
    packages=find_packages(),
    install_requires=['pandas','numpy']

)







