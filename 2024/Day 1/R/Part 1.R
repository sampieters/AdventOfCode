PATH <- "./2024/Day 1/input.txt"

# Load the text file
data <- read.table(PATH, header=FALSE, sep=" ", stringsAsFactors = FALSE)

left <- sort(data[,1])
right <- sort(data[,4])

distances <- abs(left - right)
result <- sum(distances)

print(result)