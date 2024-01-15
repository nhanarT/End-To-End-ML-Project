import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "End-to-end-ML-project"
AUTHOR_USER_NAME = "nhanarT"
SRC_REPO = "ml-project"
VERSION = "0.0.1"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    version=VERSION,
    long_description=long_description,
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
)
