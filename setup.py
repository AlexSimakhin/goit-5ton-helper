from setuptools import setup, find_namespace_packages

setup(
    name="goit-5ton-helper",
    version="1.0.0",
    description="GoIT Team project Assistant bot",
    url="https://github.com/AlexSimakhin/goit-5ton-helper",
    author="goit-5ton-helper",
    license="MIT",
    packages=find_namespace_packages(where="assistant_bot"),
    package_dir={"": "assistant_bot"},
    install_requires=["prompt_toolkit"],
    entry_points={"console_scripts": ["hi-bot=main:main"]},
)
