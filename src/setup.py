import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freshen-sorter",  # Replace with your own username
    version="1.5.12",
    author="Salvador Aleguas",
    author_email="salvadoraleguas@gmail.com",
    description="A program that sorts files based on various attributes from the (currently only windows) context menu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saleguas/freshen",
    packages=['freshen'],
    package_data={'freshen': ['config/*.yml']},
    keywords=['file', 'file-organizer',
              'context-menu', 'file-sorter', 'sorter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    install_requires=[
   'context_menu',
   'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'freshen=freshen.console_scripts:main'
        ]
    },
    python_requires='>=3.6',
)
