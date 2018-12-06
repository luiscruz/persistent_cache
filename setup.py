import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="persistent_cache",
    version="0.0.1",
    author="Luis Cruz",
    author_email="luismirandacruz@gmail.com",
    description="Function cache that uses a JSON file for persistency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luiscruz/persistent_cache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)