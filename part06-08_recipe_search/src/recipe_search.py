# Write your solution here


def search_by_name(filename: str, word: str):

    with open(filename) as new_file:

        lines = []
        recipe = []

        for line in new_file:
            if line == "\n":
                lines.append(recipe)
                recipe = []
            else:
                recipe.append(line.strip())
        else:
            lines.append(recipe)

    answer = []

    for line in lines:
        if line[0].lower().find(word) != -1:
            answer.append(line[0])

    return answer
            

def search_by_time(filename: str, prep_time: int):
    with open(filename) as new_file:

        lines = []
        recipe = []

        for line in new_file:
            if line == "\n":
                lines.append(recipe)
                recipe = []
            else:
                recipe.append(line.strip())
        else:
            lines.append(recipe)

    answer = []

    for line in lines:
        if int(line[1]) <= prep_time:
            answer.append(f'{line[0]}, preparation time {line[1]} min')

    return answer

def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as new_file:

        lines = []
        recipe = []

        for line in new_file:
            if line == "\n":
                lines.append(recipe)
                recipe = []
            else:
                recipe.append(line.strip())
        else:
            lines.append(recipe)

    answer = []

    for line in lines:
        if ingredient in line[2:]:
            answer.append(f'{line[0]}, preparation time {line[1]} min')
    
    return answer


# search_by_name("recipes1.txt", "cake")
# print(search_by_time("recipes1.txt", 20))



# a = search_by_ingredient("recipes1.txt", "eggs")

# for i in a:
#     print(i)
                