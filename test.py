"Here's a docstring"

def mainfunc():
    "Here's a docstring"
    birthdays = {}
    birthdays['Luke Skywalker'] = '5/24/19'
    birthdays['Obi-Wan Kenobi'] = '3/11/57'
    birthdays['Darth Vader'] = '4/1/41'

    for jedi in 'Yoda', 'Darth Vader':
        if jedi not in birthdays:
            birthdays[jedi] = 'unknown'

    for jedi in birthdays:
        print(jedi, birthdays[jedi])

mainfunc()
