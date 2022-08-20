"""Generate sales report showing total melons each salesperson sold."""


salespeople = []  # empty list
melons_sold = []  # empty list

f = open('sales-report.txt')  # opneing the file

for line in f:  # iterating over the file
    line = line.rstrip()  # removing white spaces
    entries = line.split('|')  # spliting the list with |
    salesperson = entries[0]  # assigning firs item to salesperson
    # assigning third item to melons and converting it to a integer
    melons = int(entries[2])

    if salesperson in salespeople:  # statment to compare info
        # adding salesperson to the empty list
        position = salespeople.index(salesperson)
        melons_sold[position] += melons  # counting the melons

    else:
        salespeople.append(salesperson)  # a ppending salesperson
        melons_sold.append(melons)  # a ppending melons


for i in range(len(salespeople)):  # printing the file
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

"""
Improvements:
    - Define a function for the whole process
    - Instead of using list, use dictionaries

"""
