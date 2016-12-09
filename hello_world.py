from test import build_profile as bp

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print(2**100)
print("create gui for python")
print(3*44)
name = "jun luo"
favoritefood = "    apple "
print favoritefood.lstrip()
print name.upper()
print name.lower()
print name.title()
print(3+5)
print(2*4)
print(17/2)
number = 3
print "my favorite number is " + str(number)
import this
bicycle = ['trek', 'cannondale', 'jiat']

print bicycle[0]
bicycle.append('newbee')
del bicycle[0]
print bicycle
print sorted(bicycle)
magicians = ['Jun', 'Luo', 'Fei', 'Ma']
for magican in magicians:
    print magican

print magican
for value in range(1,7):
    print value
even_numbers = list(range(2,11,2))

print even_numbers
cube_numbers = [value**3 for value in range(1,11)]
print cube_numbers

dimension = (5,4)
print dimension
dimension = (4,5)
print dimension

request_toppings = []
alien_0 = {'color': 'green', 'points': '3'}
print(alien_0['color'])

favorite_language = {
    'jen': 'python',
    'junluo': 'C plus plus',
    'li': 'swift'
}

print favorite_language['jen']

for name, language in favorite_language.items():
    print name.title() + "'s favorite language is " + language.title() + "."

for name in favorite_language.keys():
    print name
favorite_language = {
    'jen': ['python', 'ruby'],
    'Jun': ['C++', 'Java']

}

for name, language in favorite_language.items():
    print name + " can handle these languages: " + language[0]

jun_profile = bp(first_name='jun', last_name='luo', location='Michigan', hobbies=['swimming', 'eating', 'cooking'])
print jun_profile
