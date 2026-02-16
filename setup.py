from setuptools import find_packages, setup

setup(
    name="gigaam",
    py_modules=["gigaam"],
    version="0.1.0",
    description="GigaAM: A package for audio modeling and ASR.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    author="GigaChat Team",
    url="https://github.com/salute-developers/GigaAM/",
    license="MIT",
    packages=find_packages(include=["gigaam"]),
    python_requires=">=3.10",
    install_requires=[
        line.strip()
        for line in open("requirements.txt", "r", encoding="utf-8")
        if line.strip() and not line.startswith("#")
    ],
    extras_require={
        "longform": ["pyannote.audio", "torchcodec", "numba"],
        "tests": ["pytest", "pytest-cov", "scipy", "soundfile", "librosa"],
    },
    include_package_data=True,
)
