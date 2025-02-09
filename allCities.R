# Import dplyr
library(dplyr)

# Open the csv file
geo <- read.csv("C:\\Users\\matys\\Hackathon\\PolyHacks25\\geonames-all-cities-with-a-population-1000.csv",
                     sep = ";") 

# Change the column names
df <- select(geo, c('ASCII.Name', 'Country.name.EN', 'Population', 
                    'Elevation', 'DIgital.Elevation.Model', 'Coordinates'))
colnames(df) <- c('City', 'Country', 'Population', 
                  'Elevation', 'Digital.Elevation', 'Coordinates')

# Remove unrelated data and change others
df$Population[df$Population == 0] <- NA
# Replacing the NAs from the Elevation column to the value of the Digital.Elevation column
df$Elevation <- ifelse(is.na(df$Elevation), df$Digital.Elevation, df$Elevation)
# Replacing the -9999 of the Elevation and Digital.Elevation column with NA
df$Elevation[df$Elevation == -9999] <- NA
# Removing all rows with NA
df <- na.omit(df)
# Remove Digital.Elevation column
df <- df[-c(5)]
# Replace Blank Countries with NA
df$Country[df$Country == ""] <- NA

