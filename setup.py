from setuptools import setup,find_packages
from typing import List
#all data type comes from typing library

#declaring variables for setup functions
project_name="house-predictor"
Version="0.0.1"  #any version u want and change version name  after every modify
AUTHOR='Akshay Nikam'
DESCRIPTION='This is a my first ml project'
PACKAGES=find_packages()  # hard coded with ['housing'] pacakage but will create problem later so better use find package for dynamic
#inside housing we are creating package so that find package will take that files which contain init main as a package
REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements_list()->List[str]: #list[str] just define what is that function going return but first import list
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")


setup(
    name="house-predictor",
    version=Version,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #find packages does the same thing -e. thats why we remove in setup.py as above
    install_requires=get_requirements_list()

)


if __name__=="__main__":
    print(get_requirements_list())