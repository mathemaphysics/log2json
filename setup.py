import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="log2json-fauzanelka",
    version="0.0.3",
    author="Fauzan Elka",
    author_email="fauzan.elka@gmail.com",
    description="Convert log to json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fauzanelka/log2json",
    project_urls={
        "Bug Tracker": "https://github.com/fauzanelka/log2json/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
	entry_points={
		"console_scripts": [
			'log2json = log2json.__main__:main'
		]
	},
)
