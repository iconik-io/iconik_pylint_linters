import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cantemo_pylint_linters",
    version="0.0.1",
    author="Konstantin Hantsov",
    author_email="hantsov@cantemo.com",
    description="A package that contains Cantemo linters fof pylint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://review.cantemo.com/source/cantemo_pylint_linters/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    pylint='>=2.3.1'
)