"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME=40
#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(s):
    """Thie function will calculate remaining bkaing time"""
    EXPECTED_BAKE_TIME=40
    EBT=EXPECTED_BAKE_TIME-s
    return (EBT)
def preparation_time_in_minutes(number_of_layers):
    """This funcation will calculate total time needed """
    result=number_of_layers*2
    return result  
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """This function will calculate number os layer and total time"""
    return number_of_layers * 2 + elapsed_bake_time
    #result=  number_of_layers*2
    #final_result=result+elapsed_bake_timereturn number_of_layers * 2 + elapsed_bake_time

#def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the bake time remaining.
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """



#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO (student): define the 'elapsed_time_in_minutes()' function below.



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
