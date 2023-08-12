# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell 
# prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; 
# the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for 
# the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the 
# senior or open category.

data1 = [(45,12), (55,21), (19,-2), (104,20)]

data2 = [(16,23), (73,1), (56,20), (1,-1)]


#edad >= 55 and handicap > 7
def open_or_senior(data):
    output = []
    for i in data:
        senior_condition1=False
        senior_condition2=False
        counter = 0
        for j in i:
            if (counter == 0 ) and (j >= 55):
                senior_condition1 = True
            elif (counter == 1) and (j > 7):
                senior_condition2 = True
            counter += 1
        if (senior_condition1 == True) and (senior_condition2 == True):
            output.append("Senior")
        else:
            output.append("Open")
            
            
            
    return output

print(open_or_senior(data2))