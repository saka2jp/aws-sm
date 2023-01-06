import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws-sm",
    version="1.2.0",
    author="saka2jp",
    author_email="saka2jp@gmail.com",
    description="A Python wrapper around the AWS Secrets Manager using Boto3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saka2jp/aws-sm",
    python_requires=">=3.7",
    install_requires=[
        "boto3~=1.16",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
