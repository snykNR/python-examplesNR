from setuptools import setup, find_packages

setup(

    name="example", # Replace with your username
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),

    install_requires=[
        'certifi==2022.12.7',
        'charset-normalizer==3.1.0',
        'idna==3.4',
        'requests==2.28.2',
        'urllib3==1.26.15'
    ],

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)