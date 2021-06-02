import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iconik_pylint_linters",
    version="0.0.1",
    author="Konstantin Hantsov",
    author_email="hantsov@iconik.io",
    description="A package that contains iconik linters for pylint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iconik-io/iconik_pylint_linters",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    pylint='>=2.3.1',
    zip_safe=False
)
