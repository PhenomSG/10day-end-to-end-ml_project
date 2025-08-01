'''
It is a module used to build and distribute Python packages
'''
from conda_build.skeletons.pypi import get_requirements
from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->list[str]:
    '''
    this func will return the list of requiremnets

    add -e. in requirements.txt to trigger setup.py
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(

    name='ml-proj',
    version='0.0.1',
    author='phenomsg',
    packages=find_packages(),
    #install_requires=['pandas','numpy']
    #
    install_requires = get_requirements(requirements.txt)
)







