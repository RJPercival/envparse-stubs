import setuptools

setuptools.setup(
    name="envparse-stubs",
    version="0.1",
    license="MIT",
    install_requires=["envparse>=0.2,<1"],
    packages=["envparse-stubs"],
    package_data={"envparse-stubs": ["__init__.pyi"]},
)
