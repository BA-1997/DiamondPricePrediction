from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        return requirement



setup(
    name='DiamondPricePridiction',
    version='0.0.1',
    author='Akshay',
    author_email='onebhardwaj@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()
)