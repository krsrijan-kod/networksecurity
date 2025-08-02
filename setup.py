from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            ##process each line
            for line in lines:
                requirements=line.strip()
                ##ignore empty lines and -e.
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirements_lst

setup(
    name="Network security",
    version="0.0.1",
    author="kumar srijan",
    author_email="ce220004028@iiti.ac.in",
    packages=find_packages(),
    instal_requires=get_requirements()

)
