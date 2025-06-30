from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="text-encode-decode",
    version="1.0.0",
    author="scthornton",
    description="A comprehensive tool for encoding and decoding text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scthornton/text_encode_decode",
    py_modules=["text_codec"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "text-encode-decode=text_codec:main",
        ],
    },
)
