import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent

# The text of the README file
long_description = pathlib.Path(__file__).parent.joinpath('README.md').read_text(encoding='utf-8')

setup(
    name="intersect",
    version="1.3.2",
    packages=find_packages(),
    description="Intersection Of two curves",
    long_description=long_description,
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 2.7",
    ],
)
