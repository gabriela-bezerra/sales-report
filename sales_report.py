"""Generate sales report showing total melons each salesperson sold."""


# salespeople = []  # empty list
# melons_sold = []  # empty list

# f = open('sales-report.txt')  # opneing the file

# for line in f:  # iterating over the file
#     line = line.rstrip()  # removing white spaces
#     entries = line.split('|')  # spliting the list with |
#     salesperson = entries[0]  # assigning firs item to salesperson
#     # assigning third item to melons and converting it to a integer
#     melons = int(entries[2])

#     if salesperson in salespeople:  # statment to compare info
#         # adding salesperson to the empty list
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons  # counting the melons

#     else:
#         salespeople.append(salesperson)  # a ppending salesperson
#         melons_sold.append(melons)  # a ppending melons


# for i in range(len(salespeople)):  # printing the file
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

"""
Improvements:
    - Define a functions for the whole process
    - Instead of using list, use dictionaries
    - Pass the file as an argument

"""


def get_melons_sales(filename):

    sales_report_data = open(filename)

    sales = {}

    for line in sales_report_data:
        line = line.rstrip()
        salesperson, total_sale, melons_sold = line.split("|")

        if salesperson in sales:
            sales[salesperson] += int(melons_sold)
        else:
            sales[salesperson] = int(melons_sold)

        ## Tried adding total value and total amount to the dictinonary as a list ##

        # for salesperson, reports in sales.item():
        #     print(salesperson).upper()

        #     for total, melons in reports.item():
        #         print(f'{total} - {melons} ')

        for person, melons in sales.items():
            print(f'{person} sold the total of {melons} melons')

    sales_report_data.close


get_melons_sales("sales-report.txt")
