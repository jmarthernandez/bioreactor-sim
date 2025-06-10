from setuptools import setup

setup(
    name="bioreactor_sim",
    version="0.1",
    py_modules=["bioreactor_sim"],
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "streamlit"
    ],
    entry_points={
        "console_scripts": [
            "simulate-bioreactor=bioreactor_sim:main",
        ],
    },
)
