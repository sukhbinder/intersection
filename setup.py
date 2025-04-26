import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "readme.md").read_text()

setup(
    name="intersect",
    version="1.3.2",
    packages=find_packages(),
    description="Intersection Of two curves",
    long_description=README,
    long_description_content_type="text/markdown",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    license="MIT",
    url="https://github.com/sukhbinder/intersection",
    keywords=["Intersection", "curves", "numpy"],
    install_requires=["numpy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 2.7",
    ],
)
