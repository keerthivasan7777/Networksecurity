from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    '''
    This function will return the list of requirements
    '''

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read  the lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name = "Networksecurity",
    version = "0.01",
    author = "Keerthivasan",
    author_email = "keerthivasan33311@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)