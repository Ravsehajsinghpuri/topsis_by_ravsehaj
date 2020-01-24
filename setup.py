import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsisbyravsehaj", # Replace with your own username
    version="0.0.5",
    author="Ravsehaj Singh Puri",
    author_email="ravsehajsinghpuri@gmail.com",
    description="A package for Topsis technique",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ravsehajsinghpuri/topsisbyravsehaj",
    packages=setuptools.find_packages(),
    install_requires=[
       'numpy','pandas','scipy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
