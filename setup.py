from setuptools import setup, find_packages

setup(
    name="agentmesh",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography>=41.0.0",
        "requests>=2.31.0",
        "anthropic>=0.18.0",
    ],
    python_requires=">=3.9",
)
