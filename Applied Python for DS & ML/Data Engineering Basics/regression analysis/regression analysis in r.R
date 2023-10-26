install.packages("lars")
install.packages("caret")

library(lars)
library(caret)

#load the data
data = read.csv("E:/DATA SETS/winequality-red.csv")
data

#define variables groups
x <- as.matrix(data[-12])
y <- data[, 12]

### recursive feature elimination (RFE)
# 1. generate a control object to specify the details of algorithms
control <- rfeControl(method = "repeatedcv",
                      repeats = 5,
                      verbose = T,
                      functions = lmFuncs)

# 2. Run recursive feature elimination (RFE)
rfe_result <- rfe(x, y , sizes = c(1:11), rfeControl = control)
rfe_result

# 3. update x
x <- as.matrix(data[rfe_result$optVariables])
head(x)

# ADDITIONAL MODELS #############################

# stepwise regression 
stepwise <- lars(x,y, type = "stepwise")
plot(stepwise)

# forward.stagewise
forward <- lars(x,y, type = "forward.stagewise")
plot(forward)

# least Angle regression
lar <- lars(x,y, type = "lar")
plot(lar)

# least absolute shrinkage and selection operator 
lasso <- lars(x,y, type = "lasso")
plot(lasso)






