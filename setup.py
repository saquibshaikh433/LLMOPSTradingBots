
from setuptools import setup, find_packages

setup(
    name = "trading bot",
    author="saquib",
    author_email="saquibshaikh433@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb","datasets","pypdf","python-dotenv","flask"]
)
