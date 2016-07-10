#Generators
#-----> Simple code returning the whole list

print "------Generators----------"
print "\n------ Without Generator ----------"
def sq_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)

    return result

my_list = [2,3,4,5]

print sq_numbers(my_list)


#------> Same code with generators
# generators does not hold all values in memory
# it generates result as needed
print "\n------ With Generator ----------"

def sq_numbers_g(nums):
    result = []
    for i in nums:
        yield (i*i) #yield is the keyword for Generators

my_gen_result1 = sq_numbers_g([3,5,6,7])

for num in my_gen_result1:
    print num

print "\n------ With Generator shortcut ----------"

my_gen_result = ( x*x for x in [22,34,55] )

#print my_gen_result
#lst = list(my_gen_result) # to conver generators to list

for num in my_gen_result:
    print "->{}".format(num)


print "\n------ List comprehension ----------"
#list comprehensions
# more clean and readable ways to create list

input = [1,2,3,4,5,6]

square = [num*num for num in input]

print square


#dictionary comprehensions
