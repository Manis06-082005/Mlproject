from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    # return the list of requirements
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlProject',
    version='0.1',
    packages=find_packages(),
    author='Manish Goswami',
    author_email='nathmanish174@gmail.com',
    description='End to end data science project.',
    install_requires=get_requirements('requirements.txt')
)