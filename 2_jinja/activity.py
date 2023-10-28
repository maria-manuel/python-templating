# REMINDER: Only do one challenge at a time! Save and test after every one.

print('jinja activity')

print('Challenge 1 -------------')
# Challenge 1:
# 1. As with the previous activity, create a new virtualenv using pipenv
# 2. Enter into that virtualenv
# 3. Install jinja2
# 4. Examine the following code. See if you can explain in your own words what
# every line is doing. Change the name to be your name.

from jinja2 import Template

template = Template('Hello, {{ name }}!')
result = template.render({
    'name': 'Keanu',
})
print(result)


# print('Challenge 2 -----------')
# # Challenge 2:
# # Using Challenge 1 as a clue, write the code to utilize this template to
# # render your own name, favorite color, favorite food, and favorite book.

user_information_template = Template('''
<p>Name: {{ name }}</p>
<p>Favorite color: {{ color }}</p>
<p>Favorite food: {{ food }}</p>
<p>Favorite book: {{ book }}</p>
''')

result = user_information_template.render({
    'name': 'Keanu',
    'color': 'Green',
    'food': 'Tacos',
    'book': 'Lord of the Rings'
})
print(result)


print('Challenge 3 -----------')
# Challenge 3:
# 1. Uncomment the print function invocation.
# 2. By only modifying the template code string, replace the question marks to
# add the template variables necessary to categorize the foods (do not modify
# the invocation).
# The first done is done for you.

template_code = '''
Healthy foods: {{ foods.fruit }}, {{foods.vegetable}}, {{foods.cold_dish}}
Junk foods: {{foods.sandwhich}}, {{foods.drink}}, {{foods.snack}}
'''

food_template = Template(template_code)
foods_info = {
    'fruit': 'apple',
    'vegetable': 'carrot',
    'sandwich': 'burger',
    'drink': 'mtn dew',
    'cold_dish': 'salad',
    'snack': 'doritos',
}

templated_results = food_template.render({
    'foods': foods_info
})
print(templated_results)


print('Challenge 4 -------------')
# Challenge 4:
# 1. Uncomment the print function invocation.
# 2. Add key / value pairs to the context dictionary to cause the template
# rendering process to render the HTML to a simple website, with a title,
# a single blog post title, and a single "lead-in" to a blog-post

# Hint 1: Only modify the "context" dictionary!
# Hint 2: Look for plural / singular as a clue of data types. You'll be using
# strings and lists for this activity.
# Hint 3: You might find helpful this description of built-in filters:
# https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters

# template_code = '''
# <h1>{{ title }}</h1>
# <p>My blog posts:</p>
# <h2>{{ blog_post_titles|first|title }}</h2>
# <h2>{{ blog_posts|first|truncate }}</h2>
# '''
# context = {
# }

#print(Template(template_code).render(context))

template_code = '''
<h1>{{ title }}</h1>
<p>My blog posts:</p>
<h2>{{ blog_post_titles|first|title }}</h2>
<h2>{{ blog_posts|first|truncate }}</h2>
'''
context = {
    'title': 'The Matrix Resurrections',
    'blog_post_titles': ['Project Ice-Cream', 'Chinatown Visit'],
    'blog_posts': ['Actor, Keanu Reeves, visits the San Francisco Bay Area. The Matrix is being filmed in the Financial District and Chinatown areas. There have been numerous reportings of the actor seen as humbly confident while eating ice-cream.'],
}

print(Template(template_code).render(context))


print('Challenge 5 -------------')
# Challenge 5:
# 1. Uncomment the print function invocation.
# 2. Only modify the template code: Add the filters necessary to do the thing it
# says.
# 3. The first one is done for you, and demonstrates how to comma separate a
# list of strings using the "join" filter.

# Hint: You'll have to research different filters here:
# https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters


# template_code = '''
# All noodles: {{ noodles|join(', ') }}
# Alphabetical:
# Reverse alphabetical:
# First:
# Last, with a capital letter:
# First alphabetically:
# Last alphabetically:
# Number of different types of noodles:
# '''

# noodles_list = [
#     'soba',
#     'ramen',
#     'lo mein',
#     'spaghetti',
#     'jap chae',
#     'vermicelli',
#     'gnocchi',
# ]

# results = Template(template_code).render({
#     'noodles': noodles_list,
# })

# #print(results)

template_code = '''
# All noodles: {{ noodles|join(', ') }}
# Alphabetical: {{ noodles|sort|join(', ') }}
# Reverse alphabetical: {{ noodles|sort|reverse|join(', ') }}
# First: {{noodles|first }}
# Last, with a capital letter: {{ noodles|last|title }}
# First alphabetically: {{ noodles|sort|first }}
# Last alphabetically: {{ noodles|sort|last }}
# Number of different types of noodles: {{ noodles|length }}
# '''

noodles_list = [
    'soba',
    'ramen',
    'lo mein',
    'spaghetti',
    'jap chae',
    'vermicelli',
    'gnocchi',
]

results = Template(template_code).render({
    'noodles': noodles_list,
})

print(results)



print('-------------')
# Advanced Bonus Challenge:
# 1. Examine the file "madlib.html" - How can you load this as a Jinja
# Template?
# 2. Using "input", make a game that asks the user the necessary questions to
# assemble the story from user answers.
# 3. Write the results to a new file.

