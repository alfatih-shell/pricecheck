from setuptools import setup, find_packages


setup(
    name="pricecheck",
    version="1.0.2",
    license="MIT",
    url="https://github.com/alfatih-shell/pricecheck",
    author="Alfatih-shell",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="riyanpratomo@gmail.com",
    packages=find_packages(),
    keywords="pricecheck",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    install_requires=[
        "requests",
        "urllib3",
        "dmacheck",
        "alertg",
    ],
    entry_points={
        "console_scripts": [
            "pricecheck=PriceChecker:main",
        ],
    },
    project_urls={
        "Source": "https://github.com/alfatih-shell/pricecheck",
    },
    zip_safe=False,
)
