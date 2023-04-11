"""Print out all the melons in our inventory."""


from melons import melons


def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, datas in sorted(melons.items()):
        print(f'{melon_name.upper()}')
        for catagory, data in datas.items():
            print(f'{catagory}: {data}')
        print('')


print_all_melons(melons)
