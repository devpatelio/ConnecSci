
import math
from random import sample

# support_area = Received Votes 


sample_votes = {"Vote1":{0:[1000, 2000, 3000]}}
#sample_vote_dict = {"Proposition":{Square_area:[votes]}}


def define_square_area(proposition):
    proposition_dict = sample_votes[proposition]
    contributions = list(proposition_dict.values())
    contributions = contributions[0]
    total_contributions = 0 
    for contribution in contributions:
        square_root = math.sqrt(contribution)
        total_contributions  += square_root
    
    square_area = (total_contributions) ** 2
    sample_votes[proposition] = {square_area:contributions}
    print("Square Area for {} has been updated".format(proposition))
    print(sample_votes)


def find_info_area():
    support_areas_lst = []
    sum_of_areas = 0
    for key in sample_votes.keys():
        relative_dictionary = sample_votes[key]
        relative_dict_keys = list(relative_dictionary.keys())[0]
        support_areas_lst.append(relative_dict_keys)
        sum_of_areas += relative_dict_keys

    
    
    return max(support_areas_lst), sum_of_areas
        

def support_area_tax(proposition):                                          # Helper Func
    current_support_area = list(sample_votes[proposition].keys())[0]
    minimum_tax = 0.05
    relative_support_information = find_info_area()
    largest_support = relative_support_information[0]
    sum_of_areas = relative_support_information[1]
    
    difference = current_support_area - minimum_tax
    quotient = difference / largest_support 
    maximum = max(quotient, 0)
    product = maximum * (current_support_area / sum_of_areas)
    return product 


def support_area_increase(proposition):
    proposition_dict = sample_votes[proposition]
    relative_support_area = list(proposition_dict.keys())[0]
    relative_votes = list(proposition.values())[0]
    relative_tax = support_area_tax(proposition)
    inverse_tax = (1 - relative_tax) ** 2
    new_support_difference = relative_support_area * inverse_tax
    sample_votes[proposition] = {new_support_difference : relative_votes}
    print("Support Area has changed with Tax: {sample_votes}")


# Testing Function
def test_model():
    square_val_initializer = define_square_area("Vote1")

test_model()


        
    



     
    