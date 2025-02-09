library(dplyr)
sealevel <- read_csv("C:\\Users\\matys\\Hackathon\\PolyHacks25\\archive\\sealevel.csv",
                     show_col_types = FALSE) 
x=sealevel$Year

# Adding a constant to remove all zeros from SmoothedGSML_GIA_sigremoved
sealevel$SmoothedGSML_GIA_sigremoved <- sealevel$SmoothedGSML_GIA_sigremoved -
                                      min(sealevel$SmoothedGSML_GIA_sigremoved)


# No GIA
# Plot of time/sea level
y1=sealevel$SmoothedGSML_GIA_sigremoved
plot(x,y1)
modele_lineaire1 <- lm(y1 ~ x)
abline(modele_lineaire1)
a1 <- modele_lineaire1[["coefficients"]][["x"]]
b1 <- modele_lineaire1[["coefficients"]][["(Intercept)"]]

# Residues
res1 <- resid(modele_lineaire1)
plot(res1 ~ x)
abline(0, 0)

# Sea Level Data frame, mean of the data of a year
sealevel_mean <- sealevel[c(1,9)]
sealevel_mean <- sealevel_mean %>%
  group_by(Year) %>%
  summarise(mean_value = mean(SmoothedGSML_GIA_sigremoved))
ym <- sealevel_mean$mean_value
xm <- sealevel_mean$Year

# Plot of the year/mean height of the water
plot(ym ~ xm)
modele_lineaireM <- lm(ym ~ xm)
abline(modele_lineaireM)
am <- modele_lineaireM[["coefficients"]][["xm"]]
bm <- modele_lineaireM[["coefficients"]][["(Intercept)"]]

# Residues des moyennes
resm <- resid(modele_lineaireM)
plot(resm ~ xm)
abline(0, 0)
# ressemble à une quadratique

# Sqrt des moyennes
yms <- ym^0.75
plot(yms ~ xm)
modele_sqrt <- lm(yms ~ xm)
abline(modele_sqrt)

# Residues des racines des moyennes
resSqrt <- resid(modele_sqrt)
plot(resSqrt ~ xm)
abline(0, 0)


  # With GIA
y2=sealevel$GMSL_GIA
plot(x,y2)
modele_lineaire2 <- lm(y2 ~ x)
abline(modele_lineaire2)
a2 <- modele_lineaire2[["coefficients"]][["x"]]
b2 <- modele_lineaire2[["coefficients"]][["(Intercept)"]]

res2 <- resid(modele_lineaire2)
plot(res2 ~ x)
abline(0, 0)


