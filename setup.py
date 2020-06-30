import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ddpg-ischubert",
    version="0.0.1",
    author="Ingmar Schubert",
    author_email="mail@ingmarschubert.com",
    description="Actor-Critic RL using DDPG (Lillicrap 2015)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ischubert/ddpg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)