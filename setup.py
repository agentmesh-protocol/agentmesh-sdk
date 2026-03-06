from setuptools import setup, find_packages

setup(
    name="agentmesh-protocol",
    version="0.1.2",
    description="The communication protocol for AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/agentmesh-protocol/agentmesh-sdk",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "cryptography>=41.0.0",
        "requests>=2.31.0",
        "anthropic>=0.18.0",
        "langchain>=0.1.0",
        "langchain-anthropic>=0.1.0",
        "langchain-core>=0.1.0",
    ],
    python_requires=">=3.9",
)
