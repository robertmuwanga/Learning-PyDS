class County:
    def __init__(self, name, population, voters):
        self.name = name
        self.population = population
        self.voters = voters

def highest_turnout(data):
    highest = (data[0].name, data[0].voters / data[0].population)

    for county in data[1:] :
        turnout = county.voters / county.population
        if(turnout < highest[1]) : highest = (county.name, turnout)

    return highest

# test data
data = [
    County('allegheny', 1000490, 645469) ,
    County('philadelphia', 1134081,539069) ,
    County('montgomery', 568952, 399591) ,
    County('lancaster', 345367, 230278) ,
    County('delaware', 414031, 284538) ,
    County('chester', 319919, 230823) ,
    County('bucks', 444149, 319816)
]

result = highest_turnout(data)
print(result)
# do not remove this line!
