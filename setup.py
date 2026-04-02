from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='data_science_project',
    version='0.1',
    package_dir={"": "src"},   #THIS LINE IS MISSING
    packages=find_packages(where="src"),
    author='Manish Goswami',
    author_email='nathmanish174@gmail.com',
    description='End to end data science project.',
    install_requires=get_requirements('requirements.txt')
)