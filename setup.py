# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


setup(
    name="tutorial",
    version="0.0.1",
    description="Use to manage python_tutorial",
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    install_requires=[
       "alembic==1.0.7",
       "requests==2.21.0",
       "PyYAML==5.1",
       "SQLAlchemy==1.3.3",
       "nameko==3.0.0-rc8",
       "marshmallow==2.19.5",
       "mysql-connector-python==8.0.16",
       "elasticsearch-dsl>=7.0.0,<8.0.0",
       "redis==3.3.11",
       "pycountry>=19.8.18",
       "SQLAlchemy-Utils==0.36.5",
       "sshtunnel==0.1.5",
       "boto3==1.14.25",
       "pycryptodome==3.9.8",
       "tqdm==4.54.0",
    ],
    extras_require={
        "dev": [
            "flake8>=3.7.7",
            "pytest==4.5.0",
            "coverage==4.5.3",
            "mock==2.0.0",
            "behave==1.2.6",
            "black==20.8b1",
        ]
    },
    zip_safe=True
)
