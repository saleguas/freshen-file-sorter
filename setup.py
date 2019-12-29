import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freshen-sorter", # Replace with your own username
    version="1.3.2",
    author="Salvador Aleguas",
    author_email="salvadoraleguas@gmail.com",
    description="A program that sorts files based on various attributes from the (currently only windows) context menu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saleguas/freshen",
    packages=setuptools.find_packages(),
    keywords = ['file', 'file-organizer', 'context-menu', 'file-sorter', 'sorter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    entry_points = {
        'console_scripts': [
            'reginstall=dist.reginstall:install'
        ]
    },
    python_requires='>=3.6',
)
