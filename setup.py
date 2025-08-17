from setuptools import find_packages, setup

from version import __version__

DATA = [
    "*.md",
    "static/*.js",
    "templates/*.html",
    "templates/auth/*.html",
]


def find_requirements() -> list[str]:
    with open("requirements.txt") as f:
        lines = f.read().splitlines()
    filtered = [x for x in lines if x and not x.startswith(("#", "git+"))]
    return filtered


setup(
    name="web-blueprint-auth",
    url="https://github.com/esherpaio/web-blueprint-auth",
    version=__version__,
    author="H.P. Mertens",
    python_requires=">=3.11",
    install_requires=find_requirements(),
    include_package_data=True,
    package_data={"": DATA},
    packages=find_packages(include=["bp_auth", "bp_auth.*"]),
)
