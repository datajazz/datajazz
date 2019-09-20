import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datajazz",
    version="0.0.3",
    author="The DataJazz Authors",
    author_email="getdatajazz@gmail.com",
    description="Tools to jazz up your data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datajazz/datajazz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='modeling fit feature engineering data science machine learning',
    install_requires=[
        'pandas',
    ],
)