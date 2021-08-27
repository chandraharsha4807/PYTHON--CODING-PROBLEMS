'''
def fruit_count(input_list):
  """
  find the  count of the given items in the list
  Args:
    :list of fruits(simple list or nested lists)
    
  Returns:
    :out_put(dict)
    
  Example:
  input_list = ['orange', 'mango', 'apple', 'orange', 'mango', 'apple',['orange', 'mango', 'apple','orange', 'mango', 'apple',['orange', 'mango', 'apple',],'apple', 'orange', 'mango', 'apple'],'orange', 'mango', 'apple']
    
    :output: {"orange":7, "apple":8, "mango":7}

'''             
out = [] 
def remove_nested(input_list):
    for i in input_list:
         if type(i) == list:
             remove_nested(i)
         else:
             out.append(i)
             

input_list = ['orange', 'mango', 'apple', 'orange', 'mango', 'apple',['orange', 'mango', 'apple','orange', 'mango', 'apple',['orange', 'mango', 'apple',],'apple', 'orange', 'mango', 'apple'],'orange', 'mango', 'apple']

remove_nested(input_list)

#print(out)
count = 0

print(dict((i,out.count(i))for i in out))
