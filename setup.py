import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="HarpBot-fergujm2",
  version="0.0.1",
  author="James Ferguson",
  author_email="james.m.ferguson@vanderbilt.edu",
  description="Plotting and computing tools for the HarpBot drawing robot",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/medlabprojects/HarpBot",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)