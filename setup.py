import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_cainowicki", # Replace with your own username
    version="0.0.6",
    author="Cai Nowicki",
    author_email="author@example.com",
    description="My Lambdata package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dunkelweizen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['sklearn', 'pandas', 'numpy']
)