require('RColorBrewer')
SLmatrix <- read.csv('dedupematrix.csv')
attach(SLmatrix)

# logit1 <- glm(formula=isnewyorker ~ BrooklynMuseum, data=SLmatrix, family=binomial)
# summary(logit1)
# 
# summary(SLmatrix)
# coef(logit1)

newyorkers <- subset(SLmatrix, isnewyorker == 1)

nonNYandUnKnown <- subset(SLmatrix, isnewyorker == 0)

# require('graphics')
# logitnewyorkers <- glm(formula=isnewyorker ~ Brokelyn + BrooklynBased + BrooklynMuseum + BrooklynNets + citibikenyc + columbia + EmpireStateBldg + FDNY + giants + gothamist + Mets + MTA + nycgov + NYCMayorsOffice + NYCParks + NYCTBus + NYCTSubway + nydailynews + nyjets + NYKnicks + NYMag + NYPDNews + nypost + nyrangers + nyuniversity + TimeOutNewYork + yankees, data=SLmatrix, family=binomial)
# summary(logitnewyorkers)
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

NONtotalBrokelyn <- sum(nonNYandUnKnown$Brokelyn)
NONtotalBrooklynMuseum <- sum(nonNYandUnKnown$BrooklynMuseum)
NONtotalBrooklynBased <- sum(nonNYandUnKnown$BrooklynBased)
NONtotalBrooklynNets <- sum(nonNYandUnKnown$BrooklynNets)
NONtotalCitibikenyc <- sum(nonNYandUnKnown$citibikenyc)
NONtotalcolumbia <- sum(nonNYandUnKnown$columbia)
NONtotalEmpireStateBldg <- sum(nonNYandUnKnown$EmpireStateBldg)
NONtotalFDNY <- sum(nonNYandUnKnown$FDNY)
NONtotalgiants <- sum(nonNYandUnKnown$giants)
NONtotalgothamist <- sum(nonNYandUnKnown$gothamist)
NONtotalMets <- sum(nonNYandUnKnown$Mets)
NONtotalMTA <- sum(nonNYandUnKnown$MTA)
NONtotalnycgov <- sum(nonNYandUnKnown$nycgov)
NONtotalNYCMayorsOffice <- sum(nonNYandUnKnown$NYCMayorsOffice)
NONtotalNYCParks <- sum(nonNYandUnKnown$NYCParks)
NONtotalNYCTBus <- sum(nonNYandUnKnown$NYCTBus)
NONtotalNYCTSubway <- sum(nonNYandUnKnown$NYCTSubway)
NONtotalnydailynews <- sum(nonNYandUnKnown$nydailynews)
NONtotalnyjets <- sum(nonNYandUnKnown$nyjets)
NONtotalNYKnicks <- sum(nonNYandUnKnown$NYKnicks)
NONtotalNYMag <- sum(nonNYandUnKnown$NYMag)
NONtotalNYPDNews <- sum(nonNYandUnKnown$NYPDNews)
NONtotalnypost <- sum(nonNYandUnKnown$nypost)
NONtotalnyrangers <- sum(nonNYandUnKnown$nyrangers)
NONtotalnyuniversity <- sum(nonNYandUnKnown$nyuniversity)
NONtotalTimeOutNewYork <- sum(nonNYandUnKnown$TimeOutNewYork)
NONtotalyankees <- sum(nonNYandUnKnown$yankees)

barplot(height=c(NONtotalBrokelyn, NONtotalBrooklynBased, NONtotalBrooklynMuseum, 
                 NONtotalBrooklynNets, NONtotalCitibikenyc, NONtotalcolumbia, NONtotalEmpireStateBldg, NONtotalFDNY,
                 NONtotalgiants, NONtotalgothamist, NONtotalMets, NONtotalMTA, NONtotalnycgov, NONtotalNYCMayorsOffice, 
                 NONtotalNYCParks, NONtotalNYCTBus, NONtotalNYCTSubway, NONtotalnydailynews, NONtotalnyjets, NONtotalNYKnicks, 
                 NONtotalNYMag, NONtotalNYPDNews, NONtotalnypost, NONtotalnyrangers, NONtotalnyuniversity, NONtotalTimeOutNewYork, 
                 NONtotalyankees), names.arg=(c('Brokelyn', 'BrooklynBased', 'BrooklynMuseum', 
                                             'BrooklynNets', 'citibikenyc', 'columbia', 'EmpireStateBldg', 'FDNY', 'giants', 'gothamist',
                                             'Mets', 'MTA', 'nycgov', 'NYCMayorsOffice', 'NYCParks', 'NYCTBus', 'NYCTSubway', 'nydailynews',
                                             'nyjets', 'NYKnicks', 'NYMag', 'NYPDNews', 'nypost', 'nyrangers', 'nyuniversity', 'TimeOutNewYork',
                                             'yankees')), horiz=TRUE, col=brewer.pal(12, name="Set3"), main='Non-New Yorkers and Unknown')

justSLmatrix <- subset(SLmatrix, select= -c(isnewyorker, UserID))
justSLnewyorkers <- subset(newyorkers, select = -c(isnewyorker, UserID))
justSLnonandunknown <- subset(nonNYandUnKnown, select = -c(isnewyorker, UserID))

justSLmatrix$nSLfollowed <- apply(justSLmatrix, 1, sum)
justSLnewyorkers$nSLfollowed <- apply(justSLnewyorkers, 1, sum)
justSLnonandunknown$nSLfollowed <- apply(justSLnonandunknown, 1, sum)

hist((subset(justSLmatrix$nSLfollowed, subset = (justSLmatrix$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks followed' )
hist((subset(justSLnewyorkers$nSLfollowed, subset = (justSLnewyorkers$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks new yorkers followed' )
hist((subset(justSLnonandunknown$nSLfollowed, subset = (justSLnonandunknown$nSLfollowed> 0))), breaks=27, main='Histogram of number of social\n landmarks non-new yorkers and\n unknowns followed' )
