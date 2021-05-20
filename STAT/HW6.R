library(lattice)
#Question 2
#a)
# mk list of scores
scores <- c(57,66,69,71,72,73,74,77,78,78,79,79,81,81,82,83,83,88,89,94)
# show boxplot
bwplot(scores)
#b)
# box-midpoint is mean 
mu <- mean(scores)
print(mu)
# Quantiles 
quarts <- quantile(scores)
q1 <- quarts['25%']
q3 <- quarts['75%']
print(q1)
print(q3)
#c)
# ICR is the quartile range 
# i.e diff btw 75th and 25th 
icr <- q3 - q1 
epsilon <- (icr*1.5)
icr_max <- mu + epsilon 
icr_min <- mu - epsilon 
print(icr_min)
print(icr_max)

# Filter by two conditions  
clean_scores <- scores[scores >= icr_min & scores <= icr_max]
print(clean_scores)

# - Question 3
# Make a data frame and plot
df <- data.frame(iris)
print(df)
histogram(~ Petal.Length,data=df)
#b)
bwplot(~Petal.Length,data=df)
#c)
histogram(~ Petal.Length | Species, data=df)
#d)
bwplot(~Sepal.Length  | Species ,data=df)
