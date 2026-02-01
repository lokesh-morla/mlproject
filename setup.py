from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Return a list of requirements from a requirements file."""
    with open(file_path) as f:
        requirements = [line.strip() for line in f if line.strip()]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="mlprojects",
    version="0.0.1",
    author="lokesh-morla",
    author_email="lokesh.srav.aadhya@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

