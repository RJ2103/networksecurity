"""
setup.py is a configuration script used to define, package, and distribute a Python project. 
It acts as the installation blueprint of the project by specifying essential metadata such as the project name, version, author, description, and Python version requirements. 
It also defines which packages or modules should be included and lists external dependencies required for the project to run.
When commands like pip install . or python setup.py install are executed, Python reads the setup.py file to understand how to build and 
install the project correctly. 
This ensures that all required libraries are installed automatically and the project structure is properly recognized as a package.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Fn will return list of requirements
    """
    try:
        requiremnet_lst: List[str] = []
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            
            for line in lines:
                requiremnet = line.strip()
                if requiremnet and requiremnet!= '-e .':
                    requiremnet_lst.append(requiremnet)

    except FileNotFoundError:
        print("requirement.txt file not found")

    return requiremnet_lst

setup(
    name="Network Security",
    version="0.0.0.1",
    author="RJ",
    author_email="rishabh.joshi2103@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)