![spacetime logo](documents/barraLogo.jpg)

## Description:
Here I document the use and progress of the spacetime python library with a series of notebooks. These range from describing suported data type to trimming data layers, creating cubes and opperating on cleaned data.

## Before Using Spacetime:
For members of the team that already use python, feel free to use the code base/future library in the way that you prefer. I will list the link to the repositiry on github and a driver script containing the loaded files and function paths at its head for your use. 

Some of us may not use python on a regular basis, so I have set up some basic instructions for getting spacetime up and running on your machines for testing purposes. The general stratagy here is to install python 3.9 or higher, create a python environment to use in R Studio using the "reticulate" package. Next, we will install the dependancies (python libraries) required to use Spacetime, clone the repository that contains the Spacetime source code, and use an R markdown template that I will provide below to use the spacetime functions. Detailed instructions for each of these steps are below. A very helpful video for walking through these steps can be found [here](https://docs.rstudio.com/tutorials/user/using-python-with-rstudio-and-reticulate/).



* 1) First, install a version of Python 3. I am using Python 3.9.12 but other later versions should also work. If you have already installed a version of python 3 on your machine but are having trouble using spacetime, you can download A newer version at the link below. Make sure you are downloading an installer for your operating system (osx/windows/linux). If you prefer, you can use a package manager like anaconda or miniconda as mentioned in the above video. They are helpful for managing python environments with different versions efficiently and cleanly. I use anaconda myself.
[Installing Python 3](https://www.python.org/downloads/)

* 2) Next we will download the code base from github. The library is at the following github link [Spacetime](https://github.com/alexburn17/spacetime_demo). You can clone it (if you opt to clone the repo, please don't push changes to your scripts to the main branch), or download it and put it in a location of your choice. I will be updating this version in a stepwise fashion, such that only fully functioning versions will be pushed to it. The downloaded/cloned folder will serve as your directory for the remainder of the python virtual environment installation.

* 3) We are going to use this python library in the R Studio environment. This IDE should allow for people with limited Python expierence who primarily work in R to smoothly transition. This page from the R Studio website gives instruction on how to set up Python 3 in R studio using the reticulate package. It requires running a few commands in your terminal. On some machines/installations the command `pip3` is used for working with Python 3 and pip is used for Python 2. The instructions below use `pip` but if you find that you are having issues and the python version you are woking with is coming up as version 2.x, try substituting the `pip3` command instead. [Working with Python 3 in R Studio](https://support.rstudio.com/hc/en-us/articles/360023654474-Installing-and-Configuring-Python-with-RStudio). 


* 4) Step 4 in the above link asks you to install python libraries that you wish to use using the `pip install`/`pip3 install` command. Here we will install python libraries required for the use of Spacetime. For the final deployment of Spacetime, dependancies that aren't already installed will autmotaically be installed but for now, we have to do this manually. The libraries you need are listed below (note, some of these libraries require eachother as dependancies. Run the intallations and if something is already installed, just check to make sure it is a recent version):
	* xarray
	* numpy
	* pandas
	* gdal
	* netCDF4
	* itertools
	* plotly_express
	* matplotlib 		



* 5) Below are templates that you can use to start working with Spacetime. I am including a traditional python script, and an R markdown file for use in R Studio. If you have gone through the above installation, use the R markdown file as your driver. These files are also located in the github repository linked in step 2. [Here](https://youtu.be/BLufWXOe_kg) is a quick video I made that shows how to interact with spacetime after python is up and running.

	* [R Markdown Driver](templates/driverTemplate.Rmd)
	* [Python Script Driver](templates/driverTemplate.py)	 

Everything should be working at this point, now you can look at the vignettes below for inspiration on how to use spacetime with your own data. This is a very early in-house version, so problems with the code are expected. When you find issues or have suggestions etc. give me a shout and I will note it and start working on a fix. If you have probems installing python and getting everything up and running, send me an email.

## Spacetime Vignettes:
When using vignettes, simply copy spacetime commands directly into your own driver. 

* [Loading Files and Making Cubes](spaceTime_vignettes/readingFiles.html)
* [Spatial Scaling](spaceTime_vignettes/scaling.html)
* [Temporal Scaling](spaceTime_vignettes/scalingTime.html)
* [Writing and Reading Cubes]()
* [Cube Operations]()
* [Plotting Cubes]()



## Documentation: 
* [API](documents/api.md)
* [PyPI Page Draft](documents/description.md)
