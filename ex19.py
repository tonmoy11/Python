#this exercise is to show how you can define variables with & w/o function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "you jave %d boxes of crackers!"  % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) #passing the arguments for the function

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 40

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even to math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And I can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)
