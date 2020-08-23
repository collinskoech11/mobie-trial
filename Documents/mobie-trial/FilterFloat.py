
import re 
  
# initialize list  
test_list = ['gfg', '45.45', 'is', '87.5', 'best', '90.34'] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# Filter float strings from String list 
# using regex + list comprehension 
temp = re.compile(r'\d+(?:\.\d*)') 
res = [ele for ele in test_list if not temp.match(ele)] 
  
# printing result 
print("String list after filtering floats : " + str(res)) 
