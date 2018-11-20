from setuptools import setup, find_packages

readme = ""
with open("README.md") as f:
    readme = f.read()

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

extras_require = {"dev": ["flake8>=3.6", "black>=18.0"]}

setup(
    name="AoCbot",
    author="sco1",
    url="https://github.com/sco1/AoCbot.git",
    version="v0.1.0",
    description="A Python Discord bot for Advent of Code",
    license="MIT",
    long_description=readme,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
    ],
)
