from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dehashed-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "dehashed=dehashed_parser.dehashed_parser:main",
        ],
    },
    author="gnome",
    author_email="gnome@groomla.ke",
    description="A cli tool to query the Dehashed API",
    long_description="A pipx-installable command-line tool to query the Dehashed API and parse the results.",
    license="MIT",
    keywords="dehashed api parser security",
    url="https://github.com/gnomegl/dehashed-cli",
    python_requires=">=3.6",
)
