library(ncdf4) # package for netcdf manipulation
library(raster) # package for raster manipulation
library(rgdal) # package for geospatial analysis
library(ggplot2) # package for plotting

nc_data <- nc_open("C:\\Users\\matys\\Hackathon\\PolyHacks25\\sst.mon.mean.nc")
nc_data2 <- nc_open("C:\\Users\\matys\\Hackathon\\PolyHacks25\\icec.mon.mean.nc")
nc_data3 <- nc_open("C:\\Users\\matys\\Hackathon\\PolyHacks25\\sst.mon.ltm.nc")
