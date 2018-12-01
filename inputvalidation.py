# Create a function with 5 parameters (3 string parameters and 2 integer parameters).
# One for the Input text
# Another for the Validation text (What it prints if its outside the boundaries)
# Another for the Error text (What it prints if there’s an error)
# A Minimum value and a Maximum value to set the boundaries of the input
# It should serve as your entire input validation, so:
# It should look for only numbers between the minimum and maximum values
# If the value is outside of the boundaries, print out the validation string
# If the value is not a number, print the error text and try it again (this can be done recursively or as a while loop)
# If the value is a number and within the boundaries, return the number
# EXTENSION:
# If the user inputs a value that’s mostly a number but has a non-numeric value in it, it ignores that non-numeric value and reads the number
# EXAMPLE:
# UserInput = “3a45”
# System reads: "345" instead of crashing because of the “a"
