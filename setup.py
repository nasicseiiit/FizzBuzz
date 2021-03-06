import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FizzBuzz",
    version="0.0.1",
    author="Nasimunni",
    author_email="nasicseiiit@gmail.com",
    description="FizzBuzz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nasicseiiit/FizzBuzz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)