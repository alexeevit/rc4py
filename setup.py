import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rc4py",
    version="0.0.1",
    author="Vyacheslav Alexeev",
    author_email="alexeev.corp@gmail.com",
    description="A small RC4 encoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexeevit/rc4py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
