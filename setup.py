from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hybrid-anime-recommender-system",
    version="0.1",
    author="Satyam",
    packages=find_packages(),
    install_requires = requirements,
)
