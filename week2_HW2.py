# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

user_list = [1, 11, 14, 5, 8, 9]


def less_than_ten(input_list):
  output_list = []
  for num in input_list:
    if num < 10:
      output_list.append(num)
  return output_list

print(less_than_ten(user_list))


# # Write a function that takes in two lists and returns the two lists merged together and sorted
# # Hint: You can use the .sort() method

list_1 = [1, 2,3,4,5,6]
list_2 = [3, 4,5,6,7,8,10]
def merge_and_sort_lists(l_1, l_2):
  merged_list = l_1 + l_2
  sorted_list = sorted(merged_list)
  return sorted_list

print(merge_and_sort_lists(list_1,list_2))
