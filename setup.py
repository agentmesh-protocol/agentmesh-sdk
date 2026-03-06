from setuptools import setup, find_packages

setup(
    name="agentmesh",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cryptography>=41.0.0",
    ],
    python_requires=">=3.9",
)
```

Commit message:
```
build: add setup.py
