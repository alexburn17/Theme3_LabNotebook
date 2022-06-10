
## Description:
Here I document the use and progress of the Spacetime Python Library with a series of notebooks. These range from describing suported data type to trimming data layers, creating cubes and opperating on cleaned data.

## Before Using Spacetime:
For members of the team that already use python, feel free to use the code base/future library in the way that you prefer. I will list the link to the repositiry on github and a driver script containing the loaded files and function paths at its head for your use. 

Some of us may not use python on a regular basis, so I have set up some basic instructions for getting Spacetime up and running on your machines. The general stratagy here is to install python 3.9, create a python environment to use in R Studio using the "reticulate" package. Next, we will install the dependancies (python libraries) required to use Spacetime, clone the repository that contains the Spacetime source code, and use an R markdown template that I will provide below to use the Spacetime functions. Detailed instructions for each of these steps are below.


* 1) First, install a version of Python 3. I am using Python 3.9.12 but other versions should also work. If you have already installed a version of python 3 on your machine but are having trouble using the package, you can download A newer version at the link below. Make sure you are downloading an installer for your operating system (osx/windows/linux)
[Installing Python 3](https://www.python.org/downloads/)

* 2) We are going to use this python library in the R Studio environment. This IDE should allow for people with limited Python expierence who primarily work in R to smoothly transition. This page from the R Studio website gives instruction on how to set up Python 3 in R studio using the reticulate package. It requires running a few commands in your terminal. On some machines/installations the command `pip3` is used for working with Python 3 and pip is used for Python 2. The instructions below use `pip` but if you find that you are having issues and the python version you are woking with is coming up as version 2.x, try substituting the `pip3` command instead. [Working with Python 3 in R Studio](https://support.rstudio.com/hc/en-us/articles/360023654474-Installing-and-Configuring-Python-with-RStudio)   

* 3) Step 4 in the above link asks you to install python libraries that you wish to use using the `pip install`/`pip3 install` command. Here we will install python libraries required for the use of Spacetime. For the final deployment of Spacetime, dependancies that aren't already installed will autmotaically be installed but for now, we have to do this manually. The libraries you need are listed below (note, some of these libraries require eachother as dependancies. Run the intallations and if something is already installed, just check to make sure it is a recent version):
	* xarray
	* numpy
	* pandas
	* gdal
	* netCDF4
	* itertools
	* plotly_express
	* matplotlib 		

* 4) Now that you have installed Python, got Python working in R Studio and installed Spacetime's dependancies, you are ready to download the code base. The library is at the following github link [Spacetime](). You can clone it, or download it and put it in your own repository. I will be updating this version in a stepwise fashion, such that only fully functioning versions will be pushed to it. If you chose to save the source code to your own reposity, just make sure that all of the code at the head of your scripts points to where you saved it.

* 5) Below are templates that you can use to start working with Spacetime. I am including a traditional python script, and an R markdown file for use in R Studio. If you have gone through the above installation, use the R markdown file as your driver.
	* [R Markdown Driver]()
	* [Python Script Driver]()	 

Everything should be working at this point, now you can look at the vignettes below for inspiration on how to use Spacetime with your own data. This is a very early inhouse version, so problems with the code are expected. When you find issued or have suggestions etc. give me a shout and I will note it and start working on a fix.

## Spacetime Vignettes:

When using vignettes, simply copy Spacetime commands directly into your own driver. The setup at the head of the vignettes are machine/installation specific and might cause errors if you copy them over too.

* [Loading Files](spaceTime_vignettes/Theme3_labNotebook.html)
* [Spatial Scaling]()
* [Temporal Scaling]()
* [Cube Operations]()
* [Plotting Cubes]()
* [Writiing and Reading Cubes]()


## Documentation: 
* [API]()
* [PyPI Page Draft]()
