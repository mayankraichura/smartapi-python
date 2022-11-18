from setuptools import setup, find_packages

about = {}
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "requests>=2.18.4",
    "six>=1.11.0",
    "python-dateutil>=2.6.1"
]

setup(
    name="msr_smartapi_python",
    version="1.3.8",
    packages=find_packages(exclude='test'),
    install_requires=requirements,
)
