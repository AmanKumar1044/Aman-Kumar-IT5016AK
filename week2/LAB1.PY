# Constants
cover_price = 24.95
discount_rate = 0.40
shipping_cost_first_copy = 3.00
shipping_cost_additional_copy = 0.75
number_of_copies = 60

# Calculate the discounted price of one book
discounted_price = cover_price * (1 - discount_rate)

# Calculate the total cost for the books
total_book_cost = discounted_price * number_of_copies

# Calculate the total shipping cost
total_shipping_cost = shipping_cost_first_copy + (number_of_copies - 1) * shipping_cost_additional_copy

# Calculate the total wholesale cost
total_wholesale_cost = total_book_cost + total_shipping_cost

print('The total wholesale cost for 60 copies is $:',total_wholesale_cost)
