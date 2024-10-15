from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = [] 
    with open(file_path) as f:
        requirements = f.readlines()
        # Clean up the list and remove the editable line if present
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements

setup(
    name='mlpackage',
    version='0.0.1',
    author='Saikiran',
    author_email='saikiranmandula1998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
