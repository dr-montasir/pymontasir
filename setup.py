from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
    name='pymontasir',
    version='0.0.1',
    description='My first python package',
    py_modules=["pymontasir"],
    package_dir={'': 'src'},
    classifiers=[
    	"Programming Language :: Python :: 3",
    	"Programming Language :: Python :: 3.7",
    	"Programming Language :: Python :: 3.8",
    	"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    	"Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dr-montasir/pymontasir",
    author="Montasir Mirghani",
    author_email="contact@montasir.me"
)