from setuptools import find_packages, setup


setup(name="aionlib",
      version="0.1.0",
      author="blueShard",
      description="Library support for the 'aion' project",
      license="MPL-2.0",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Home Automation"],
      python_requires=">=3.6.*",
      install_requires=["colorama"],
      packages=find_packages())
