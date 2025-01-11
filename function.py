#
# def find_sum_positive_numbers(numbers):
#     sum = 0
#     for i in range(0, len(numbers)):
#         if numbers[i] > 0:
#             sum += numbers[i]
#     return sum
#
#
# result = find_sum_positive_numbers([2, 4, -7, 8, -9])
# print(f"Result = {result}")

# Krijoni nje funksion qe gjen emrin me te shkurter nga nje liste me emra te dhene:
# emri: find_shortest_name
# input: names : list
# output: result
# example:
# result = find_shortest_name(["Bledi", "Ana", "Sara"])

name_list = ["Bledi", "Ana", "Sara"]
lengths = [len(item) for item in name_list]
print(lengths)


