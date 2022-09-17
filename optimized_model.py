
import math
import  matplotlib.pyplot as plt

# support_area = Received Votes 


sample_votes = {"Vote1":{0:[1000, 2000, 3000]}, "Vote2":{0:[70, 100, 300]}}
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
    minimum_tax = 1000                                                      # Value in Support Area
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
    relative_votes = list(proposition_dict.values())[0]
    relative_tax = support_area_tax(proposition)
    inverse_tax = (1 - relative_tax) ** 2
    new_support_difference = relative_support_area * inverse_tax
    sample_votes[proposition] = {new_support_difference : relative_votes}
    print("Support Area has changed with Tax: {}".format(sample_votes))


# Testing Functions

def graph_tests(array):
    plt.plot(array)
    plt.ylabel("Support Area With Tax")
    plt.xlabel("Number of Votes")
    plt.show()


def test_model():
    square_val_initializer = define_square_area("Vote1")   
    support_area_increase_test = support_area_increase("Vote1")
    print("-"*25)
    square_val_initializer2 = define_square_area("Vote2")   
    support_area_increase_test2 = support_area_increase("Vote2")

    values = list(sample_votes.values())
    test_array_of_areas = []
    for dict in values:
        key = list(dict.keys())[0]
        test_array_of_areas.append(key)
    
    graph_tests(test_array_of_areas)

test_model()




        
    



     
    