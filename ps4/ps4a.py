# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations = []
    held_letter = sequence[0]
    if len(sequence) == 1:
        permutations = held_letter
        return permutations
    else:
        shorter_permutations = get_permutations(sequence[1: len(sequence)] )
        for j in range(len(shorter_permutations)):
            for i in range(len(sequence)):  
                shorter_word = shorter_permutations[j][0:i] + held_letter + shorter_permutations[j][i: len(shorter_permutations[j]) ]
                permutations.append(shorter_word)
        permutations = list(set(permutations))
        return permutations
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print(get_permutations('abcde'), len(get_permutations('abcde')))
    