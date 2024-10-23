#program: item_indices
#author: malesela
#company: spacemilk

def counter(iterable, query):
    """returns indices of items in an iterable"""
    
    item_locations = []
    appearances = iterable.count(query)

    if appearances:
        item_locations.append(iterable.index(query))
        appearances -= 1

        while appearances:
            start_at = iterable.index(query, item_locations[-1] + 1, len(iterable) -1)
            item_locations.append(start_at)
            appearances -= 1

    return tuple(item_locations)


lst = list(range(10))
lst.extend(lst.copy())

print(counter(lst, 3))
