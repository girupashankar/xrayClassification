from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT= "-e ."


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='xrayClassification',
    version='1.0',
    description='A deep learning project for classifying X-ray images',
    author='Girupa Shankar K M',
    author_email='girupashankar20@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(r"C:\\DEMON\\Projects\\courses\\ineuron\\xrayClassification\\xrayClassification\\requirements_dev.txt"),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
