from setuptools import setup, find_packages

setup(
    name='spark_maven_demo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyspark'
    ],
    entry_points={
        'console_scripts': [
            'spark-run=spark_maven_demo.main:main'
        ]
    }
)
