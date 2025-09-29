# Timed Challenge
# Problem: Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(items):
    """
    Data structure choice: Set + List
    Reason: A set allows O(1) average lookups to track seen items,
    while a list maintains the original order.
    This combination makes sure to check uniqueness efficiently while preserving order.
    Time complexity: O(n), Space complexity: O(n).
    """
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result



if __name__ == "__main__":
    sample_input = ["apple", "banana", "apple", "kiwi", "banana"]
    print("Timed Challenge Output:")
    print(remove_duplicates_keep_order(sample_input))

# I made some tests too so I could see how it reacts in different scenarios. Such as all dupes or just an empty list  

if __name__ == "__main__":
    print("Timed Challenge: Remove Duplicates (Keep Order)\n")

    # Regular test case
    test1 = ["apple", "banana", "apple", "kiwi", "banana"]
    print("Test 1:", remove_duplicates_keep_order(test1))  # ['apple', 'banana', 'kiwi']

    # Empty list
    test2 = []
    print("Test 2 (empty list):", remove_duplicates_keep_order(test2))  # []

    # All duplicates
    test3 = ["a", "a", "a", "a"]
    print("Test 3 (all duplicates):", remove_duplicates_keep_order(test3))  # ['a']

# For the timed challenge I chose the remove duplicates and keep order question with the fruits. I used a set and a list becuase it makes it work quickly andit is relatively simple 
# The set helps check if you have already seen the value in the data and the list keeps the data in the order it appeared in (minus the duplicates of course)
# Doing it this way also only makes it have to go through the list one time
# The 30 minute time limit affects how you go about a problem because it makes you want to find a simple answer that works well rather than something
# that could be more complex and take more time to implement
# One tradeoff I made doing this was not making as many test cases as I possibly could have. I tested an empty list, a list of all dupes, and a regular list. 
# My solution works well for the example cases and typical answers but if it were a real project more safeguards should be added to ensure it always runs properly.
# This challenge showed me how important it is to quickly choose the right structure for a problem.
# It also taught me how to balance speed and accuracy when under pressure, which is needed when in a scenario like this for a technical interview! 
#