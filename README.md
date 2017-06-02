# Python Model Calculator
## Structure
### Memory
Part of the project that take the data from the sources (excel file, access db, mongodb or API ...) and create an on-demand [DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
### Brain
This part does the calculation and lookups. Requiring the data from the Memory part without knowing the sources of the data the Brain can work with any db as long as it has the right data.
### Talk
The output of the calculation. Calling suitable dimensions/formulas from Brain to provide the calculation results to various sources (files, HTTP requests ...)
## Run
1. Move this project under `site-package` under `python3.x` folder
2. Config the file `talk/fid.txt` for the list of freelancer id that you want to calculate (each freelancer id on one line)
3. Run the suitable `.py` file in the `talk` folder to see the calculation result on the `.txt` files (e.g `python3 talk/test_formulars.py`)
## Calculation Result
1. `CALCULATION.txt` shows the results after each formula
2. `RESULT.txt` shows the final results for each freelancers
## How to contribute
1. Change `Memory` to use `MSAccess` instead of `MSExcel`
2. Continue to develop other dimensions calculation in the Brain part
3. Develop the Talk part to have a feature to write back the result to `MSAccess`
## Developer
vu@cherryfish.me
