import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trellomailing",
    version="0.0.1",
    author="Jennifer C J Radtke",
    author_email="jcj.radtke@gmail.com",
    description="A package to read JSON export from a trello board and convert it into LaTeX label friendly format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RadtkeJCJ/trello-python-mailing-labels.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
