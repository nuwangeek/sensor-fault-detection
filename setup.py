from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """

    requirement_list:List[str] = []
    return requirement_list

    
setup(

    name= "sensor",
    version= "0.0.1",
    author= "bimsara",
    author_email= "charithym321@gmail.com",
    packages= find_packages(),
    install_requires= ["pymongo==4.2.0"]
)