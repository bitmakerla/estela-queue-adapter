from setuptools import find_packages, setup

setup(
    name="estela-queue-adapter",
    version="0.1",
    description="Queue adapter for estela",
    packages=find_packages(),
    install_requires=[
        "kafka-python",
    ],
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
