
![Spacetime logo](img/barraLogo.png)


-----------------

# Spacetime Known Issues

Spacetime is still in development and issues with installation and use may arise from time to time. Here we document some known issues and some work-arounds to get you back to cleaning your raster data!



### - 00Lock Error:
On occasion and on some machines, an error claiming the inability to change the working directory will be thrown upon installation. A second attempt to install spacetime will results in a 00Lock error. Removing the 00Lock folder in the spacetime installation directory and a reinstall will solve this issue. The directory will to the library and 00Lock file will be displayed in this error. Open the directory and delete the file.

```bash
open path/to/file/library

```


### - First Installation:
For users who have never installed python via miniconda and the subsequent python dependancies, the first installation may take some time. This may be exacerbated by an older, slower machine and/or a slow connection. Future installations will much quicker. 

### - Indirect Paths:
Indirect paths are currently inefective in the R version of Spacetime producing file not found errors. Direct paths are the only method for pointing to files at this point. A fix for this problem is coming soon. Until that point, direct paths will function.





