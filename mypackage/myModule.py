def top_n (items, n):
    """
    Returns the top n items in an array in descending order

    Args:
        items(array): list or an array-like object
        n(int): num items to be returned

    Return:
        array:top n items in descending order

    Egs:
        >>>top_n([8,3,2,7,4], 3)
        [8,7,4]

    """

for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!
                
# Get last two items
top_n = items[-n:]
    
# Return in descending order
return top_n[::-1]