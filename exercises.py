digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf']

new_dict = {}
for num in range(0, len(digits)):
    curr_num = digits[num]
    new_dict[curr_num] = {'french': fr[num], 'english': en[num]}

print(new_dict)
