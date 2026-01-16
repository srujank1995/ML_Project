from setuptools import find_packages, setup
from typing import List

E_DOT= '-e .'

def get_requirments(file_path:str)->List[str]:
    """
    Docstring for get_requirments
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    """
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n','') for req in requirments]

        if E_DOT in requirments:
            requirments.remove(E_DOT)

    return requirments

setup(
    name="ML_Project",
    version="0.0.1",
    author="SrujanK",
    author_email="srujankinjawadekar1@gmail.com",
    packages=find_packages(),
    install_require = ['requirments.txt']

)