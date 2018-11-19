def verify(number) :
    number_of_rules_passed = 0
    number_list = [num for num in number if num.isnumeric()]
    
#    print('Executing rules for {}'.format(number))
    
    try: 
        if int(number_list[0]) == 4 : 
            number_of_rules_passed += 1
        else :
            raise ValueError(1) 

        # Rule 2
        if (int(number_list[3]) - int(number_list[4])  == 1) : 
            number_of_rules_passed += 1  
        else : 
            raise ValueError(2)

        # Rule 3
        if (sum(map(int, number_list)) % 4 == 0) : 
            number_of_rules_passed += 1 
        else :
            raise ValueError(3)

        # Rule 4
        if sum(list(map(lambda x : int(''.join(x)), [number_list[:2], number_list[6:8]]))) == 100 : 
            number_of_rules_passed += 1 
        else :
            raise ValueError(4)
    
    except ValueError as e: 
        if e.args[0] == 1:
            return '"{}": violates rule #{}'.format(number, e.args[0])
        elif number_of_rules_passed == 1:
            return '"{}": passes rule #{}, violates rule #{}'.format(number, number_of_rules_passed, e.args[0])
        else :
            return '"{}": passes rules #1-{}, violates rule #{}'.format(number, number_of_rules_passed, e.args[0])
    
    return '"{}": passes all rules'.format(number)

input = ['5000-0000-0000', '4000-0000-0000', '4007-6000-0000', '4037-6000-0000', '4094-3460-2754']

for item in input: 
    print(verify(item))
# do not remove this line!