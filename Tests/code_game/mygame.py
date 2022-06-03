# def game(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return 'Romeo and Juliet'
#     elif number % 3 == 0:
#         return 'cheese'
#     elif number % 5 == 0:
#         return 'guava'
#     else:
#         return number

def game(number):
    return ['Romeo and Juliet' if number%3 == 0 and number%5 == 0 else \
     'cheese' if number % 3 == 0 else 'guava' if number % 5 == 0 else number][0]
