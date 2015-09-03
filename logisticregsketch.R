require('RColorBrewer')
SLmatrix <- read.csv('mastermatrix1.csv')
attach(SLmatrix)

# logit1 <- glm(formula=isnewyorker ~ BrooklynMuseum, data=SLmatrix, family=binomial)
# summary(logit1)
# 
# summary(SLmatrix)
# coef(logit1)

newyorkers <- subset(SLmatrix, isnewyorker == 1)
nonNYandUnKnown <- subset(SLmatrix, isnewyorker == 0)
nonNY <- subset(nonNYandUnKnown, haslocationtext == 1)
unknown <- subset(nonNYandUnKnown, haslocationtext == 0)

# require('graphics')
# logitnewyorkers <- glm(formula=isnewyorker ~ Brokelyn + BrooklynBased + BrooklynMuseum + BrooklynNets + citibikenyc + columbia + EmpireStateBldg + FDNY + giants + gothamist + Mets + MTA + nycgov + NYCMayorsOffice + NYCParks + NYCTBus + NYCTSubway + nydailynews + nyjets + NYKnicks + NYMag + NYPDNews + nypost + nyrangers + nyuniversity + TimeOutNewYork + yankees, data=SLmatrix, family=binomial)
logitnewyorkers <- glm(formula=SLmatrix$isnewyorker ~ SLmatrix$Brokelyn + SLmatrix$BrooklynBased + SLmatrix$BrooklynMuseum + SLmatrix$BrooklynNets + SLmatrix$citibikenyc + SLmatrix$columbia + SLmatrix$EmpireStateBldg + SLmatrix$FDNY + SLmatrix$giants + SLmatrix$gothamist + SLmatrix$Mets + SLmatrix$MTA + SLmatrix$nycgov + SLmatrix$NYCMayorsOffice + SLmatrix$NYCParks + SLmatrix$NYCTBus + SLmatrix$NYCTSubway + SLmatrix$nydailynews + SLmatrix$nyjets + SLmatrix$NYKnicks + SLmatrix$NYMag + SLmatrix$NYPDNews + SLmatrix$nypost + SLmatrix$nyrangers + SLmatrix$nyuniversity + SLmatrix$TimeOutNewYork + SLmatrix$yankees, data=SLmatrix, family=binomial)
summary(logitnewyorkers)
# plot(coef(logitnewyorkers)) 
# text(coef(logitnewyorkers), labels=names(residuals(logitnewyorkers)))

totalNewYorkers <- sum(newyorkers$isnewyorker)
totalBrokelyn <- sum(newyorkers$Brokelyn)
totalBrooklynMuseum <- sum(newyorkers$BrooklynMuseum)
totalBrooklynBased <- sum(newyorkers$BrooklynBased)
totalBrooklynNets <- sum(newyorkers$BrooklynNets)
totalCitibikenyc <- sum(newyorkers$citibikenyc)
totalcolumbia <- sum(newyorkers$columbia)
totalEmpireStateBldg <- sum(newyorkers$EmpireStateBldg)
totalFDNY <- sum(newyorkers$FDNY)
totalgiants <- sum(newyorkers$giants)
totalgothamist <- sum(newyorkers$gothamist)
totalMets <- sum(newyorkers$Mets)
totalMTA <- sum(newyorkers$MTA)
totalnycgov <- sum(newyorkers$nycgov)
totalNYCMayorsOffice <- sum(newyorkers$NYCMayorsOffice)
totalNYCParks <- sum(newyorkers$NYCParks)
totalNYCTBus <- sum(newyorkers$NYCTBus)
totalNYCTSubway <- sum(newyorkers$NYCTSubway)
totalnydailynews <- sum(newyorkers$nydailynews)
totalnyjets <- sum(newyorkers$nyjets)
totalNYKnicks <- sum(newyorkers$NYKnicks)
totalNYMag <- sum(newyorkers$NYMag)
totalNYPDNews <- sum(newyorkers$NYPDNews)
totalnypost <- sum(newyorkers$nypost)
totalnyrangers <- sum(newyorkers$nyrangers)
totalnyuniversity <- sum(newyorkers$nyuniversity)
totalTimeOutNewYork <- sum(newyorkers$TimeOutNewYork)
totalyankees <- sum(newyorkers$yankees)

par(las=2)
par(mar=c(5,8,4,2))

barplot(height=c(totalBrokelyn, totalBrooklynBased, totalBrooklynMuseum, 
totalBrooklynNets, totalCitibikenyc, totalcolumbia, totalEmpireStateBldg, totalFDNY,
totalgiants, totalgothamist, totalMets, totalMTA, totalnycgov, totalNYCMayorsOffice, 
totalNYCParks, totalNYCTBus, totalNYCTSubway, totalnydailynews, totalnyjets, totalNYKnicks, 
totalNYMag, totalNYPDNews, totalnypost, totalnyrangers, totalnyuniversity, totalTimeOutNewYork, 
totalyankees), names.arg=(c('Brokelyn', 'BrooklynBased', 'BrooklynMuseum', 
'BrooklynNets', 'citibikenyc', 'columbia', 'EmpireStateBldg', 'FDNY', 'giants', 'gothamist',
'Mets', 'MTA', 'nycgov', 'NYCMayorsOffice', 'NYCParks', 'NYCTBus', 'NYCTSubway', 'nydailynews',
'nyjets', 'NYKnicks', 'NYMag', 'NYPDNews', 'nypost', 'nyrangers', 'nyuniversity', 'TimeOutNewYork',
'yankees')), horiz=TRUE, col=brewer.pal(12, name="Set3"), legend=TRUE, main='New Yorkers')


# col.sums <- apply(SLmatrix, 2, sum)
# 
# newdata = subset(SLmatrix[,2:29], isnewyorker==1)
# newdata2 = subset(SLmatrix[,2:29], isnewyorker==0)
# 
# class(SLmatrix$UserIDorig)
# SLmatrix$UserIDorig <- SLmatrix$UserID
# 
# SLmatrix$UserID <- as.numeric(SLmatrix$UserID)
# 
# weirds <- subset(SLmatrix, UserID != UserIDorig)
# 
# newdata$predictNYers <- predict(logitnewyorkers, newdata=newdata, type='response')
# newdata2$predictNYers <-predict(logitnewyorkers, newdata=newdata2, type='response')
# 
# summary(newdata$predictNYers)
# summary(newdata2$predictNYers)

#people who have location text, but it isn't in NY
NONtotalBrokelyn <- sum(nonNY$Brokelyn)
NONtotalBrooklynMuseum <- sum(nonNY$BrooklynMuseum)
NONtotalBrooklynBased <- sum(nonNY$BrooklynBased)
NONtotalBrooklynNets <- sum(nonNY$BrooklynNets)
NONtotalCitibikenyc <- sum(nonNY$citibikenyc)
NONtotalcolumbia <- sum(nonNY$columbia)
NONtotalEmpireStateBldg <- sum(nonNY$EmpireStateBldg)
NONtotalFDNY <- sum(nonNY$FDNY)
NONtotalgiants <- sum(nonNY$giants)
NONtotalgothamist <- sum(nonNY$gothamist)
NONtotalMets <- sum(nonNY$Mets)
NONtotalMTA <- sum(nonNY$MTA)
NONtotalnycgov <- sum(nonNY$nycgov)
NONtotalNYCMayorsOffice <- sum(nonNY$NYCMayorsOffice)
NONtotalNYCParks <- sum(nonNY$NYCParks)
NONtotalNYCTBus <- sum(nonNY$NYCTBus)
NONtotalNYCTSubway <- sum(nonNY$NYCTSubway)
NONtotalnydailynews <- sum(nonNY$nydailynews)
NONtotalnyjets <- sum(nonNY$nyjets)
NONtotalNYKnicks <- sum(nonNY$NYKnicks)
NONtotalNYMag <- sum(nonNY$NYMag)
NONtotalNYPDNews <- sum(nonNY$NYPDNews)
NONtotalnypost <- sum(nonNY$nypost)
NONtotalnyrangers <- sum(nonNY$nyrangers)
NONtotalnyuniversity <- sum(nonNY$nyuniversity)
NONtotalTimeOutNewYork <- sum(nonNY$TimeOutNewYork)
NONtotalyankees <- sum(nonNY$yankees)

barplot(height=c(NONtotalBrokelyn, NONtotalBrooklynBased, NONtotalBrooklynMuseum, 
                 NONtotalBrooklynNets, NONtotalCitibikenyc, NONtotalcolumbia, NONtotalEmpireStateBldg, NONtotalFDNY,
                 NONtotalgiants, NONtotalgothamist, NONtotalMets, NONtotalMTA, NONtotalnycgov, NONtotalNYCMayorsOffice, 
                 NONtotalNYCParks, NONtotalNYCTBus, NONtotalNYCTSubway, NONtotalnydailynews, NONtotalnyjets, NONtotalNYKnicks, 
                 NONtotalNYMag, NONtotalNYPDNews, NONtotalnypost, NONtotalnyrangers, NONtotalnyuniversity, NONtotalTimeOutNewYork, 
                 NONtotalyankees), names.arg=(c('Brokelyn', 'BrooklynBased', 'BrooklynMuseum', 
                                             'BrooklynNets', 'citibikenyc', 'columbia', 'EmpireStateBldg', 'FDNY', 'giants', 'gothamist',
                                             'Mets', 'MTA', 'nycgov', 'NYCMayorsOffice', 'NYCParks', 'NYCTBus', 'NYCTSubway', 'nydailynews',
                                             'nyjets', 'NYKnicks', 'NYMag', 'NYPDNews', 'nypost', 'nyrangers', 'nyuniversity', 'TimeOutNewYork',
                                             'yankees')), horiz=TRUE, col=brewer.pal(12, name="Set3"), main='Non-New Yorkers')

#users with no location text
unknowntotalBrokelyn <- sum(unknown$Brokelyn)
unknowntotalBrooklynMuseum <- sum(unknown$BrooklynMuseum)
unknowntotalBrooklynBased <- sum(unknown$BrooklynBased)
unknowntotalBrooklynNets <- sum(unknown$BrooklynNets)
unknowntotalCitibikenyc <- sum(unknown$citibikenyc)
unknowntotalcolumbia <- sum(unknown$columbia)
unknowntotalEmpireStateBldg <- sum(unknown$EmpireStateBldg)
unknowntotalFDNY <- sum(unknown$FDNY)
unknowntotalgiants <- sum(unknown$giants)
unknowntotalgothamist <- sum(unknown$gothamist)
unknowntotalMets <- sum(unknown$Mets)
unknowntotalMTA <- sum(unknown$MTA)
unknowntotalnycgov <- sum(unknown$nycgov)
unknowntotalNYCMayorsOffice <- sum(unknown$NYCMayorsOffice)
unknowntotalNYCParks <- sum(unknown$NYCParks)
unknowntotalNYCTBus <- sum(unknown$NYCTBus)
unknowntotalNYCTSubway <- sum(unknown$NYCTSubway)
unknowntotalnydailynews <- sum(unknown$nydailynews)
unknowntotalnyjets <- sum(unknown$nyjets)
unknowntotalNYKnicks <- sum(unknown$NYKnicks)
unknowntotalNYMag <- sum(unknown$NYMag)
unknowntotalNYPDNews <- sum(unknown$NYPDNews)
unknowntotalnypost <- sum(unknown$nypost)
unknowntotalnyrangers <- sum(unknown$nyrangers)
unknowntotalnyuniversity <- sum(unknown$nyuniversity)
unknowntotalTimeOutNewYork <- sum(unknown$TimeOutNewYork)
unknowntotalyankees <- sum(unknown$yankees)

barplot(height=c(unknowntotalBrokelyn, unknowntotalBrooklynBased, unknowntotalBrooklynMuseum, 
                 unknowntotalBrooklynNets, unknowntotalCitibikenyc, unknowntotalcolumbia, unknowntotalEmpireStateBldg, unknowntotalFDNY,
                 unknowntotalgiants, unknowntotalgothamist, unknowntotalMets, unknowntotalMTA, unknowntotalnycgov, unknowntotalNYCMayorsOffice, 
                 unknowntotalNYCParks, unknowntotalNYCTBus, unknowntotalNYCTSubway, unknowntotalnydailynews, unknowntotalnyjets, unknowntotalNYKnicks, 
                 unknowntotalNYMag, unknowntotalNYPDNews, unknowntotalnypost, unknowntotalnyrangers, unknowntotalnyuniversity, unknowntotalTimeOutNewYork, 
                 unknowntotalyankees), names.arg=(c('Brokelyn', 'BrooklynBased', 'BrooklynMuseum', 
                                                    'BrooklynNets', 'citibikenyc', 'columbia', 'EmpireStateBldg', 'FDNY', 'giants', 'gothamist',
                                                    'Mets', 'MTA', 'nycgov', 'NYCMayorsOffice', 'NYCParks', 'NYCTBus', 'NYCTSubway', 'nydailynews',
                                                    'nyjets', 'NYKnicks', 'NYMag', 'NYPDNews', 'nypost', 'nyrangers', 'nyuniversity', 'TimeOutNewYork',
                                                    'yankees')), horiz=TRUE, col=brewer.pal(12, name="Set3"), main='Unknown -- no location text')



justSLmatrix <- subset(SLmatrix, select= -c(isnewyorker, UserID))
justSLnewyorkers <- subset(newyorkers, select = -c(isnewyorker, UserID))
justSLnonandunknown <- subset(nonNYandUnKnown, select = -c(isnewyorker, UserID))
justSLnonNY <- subset(nonNY, select = -c(isnewyorker, UserID))
justSLunknown <- subset(unknown, select = -c(isnewyorker, UserID))


justSLmatrix$nSLfollowed <- apply(justSLmatrix, 1, sum)
justSLnewyorkers$nSLfollowed <- apply(justSLnewyorkers, 1, sum)
justSLnonandunknown$nSLfollowed <- apply(justSLnonandunknown, 1, sum)
justSLnonNY$nSLfollowed <- apply(justSLnonNY, 1, sum)
justSLunknown$nSLfollowed <- apply(justSLunknown, 1, sum)

par(xaxp = c(1, 27, 5))
par(mar=c(8,6,4,2))


hist((subset(justSLmatrix$nSLfollowed, subset = (justSLmatrix$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks followed', xlab='number of social landmarks followed')
hist((subset(justSLnewyorkers$nSLfollowed, subset = (justSLnewyorkers$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks new yorkers followed', xlab='number of social landmarks followed')
hist((subset(justSLnonandunknown$nSLfollowed, subset = (justSLnonandunknown$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks non-new yorkers and\n unknowns followed', xlab='number of social landmarks followed')
hist((subset(justSLnonNY$nSLfollowed, subset = (justSLnonNY$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks non-new yorkers\n followed', xlab='number of social landmarks followed')
hist((subset(justSLunknown$nSLfollowed, subset = (justSLunknown$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks unknown location\n users followed', xlab='number of social landmarks followed')


# ---------- predicting with logit things
# newdata = justSLunknown
# newdata$predictNYers <- predict(logitnewyorkers, newdata=newdata, type='response')
# newdata2$predictNYers <-predict(logitnewyorkers, newdata=newdata2, type='response')
# 
# summary(newdata$predictNYers)
# summary(newdata2$predictNYers)