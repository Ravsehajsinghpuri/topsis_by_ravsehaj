import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis_by_ravsehaj", # Replace with your own username
    version="0.0.1",
    author="Ravsehaj Singh Puri",
    author_email="ravsehajsinghpuri@gmail.com",
    description="A package for Topsis technique",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ravsehajsinghpuri/topsis_by_ravsehaj",
    packages=setuptools.find_packages(),
    install_requires=[
        'sys','numpy','pandas','math','scipy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
