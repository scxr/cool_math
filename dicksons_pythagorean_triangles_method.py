"""
To generate my pythagorean triples i will be using dicksons method, see here:
https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
r,s,t such that r^2 = 2st
x = r+s
y = r+t
z = r+s+t
our triplet is then of course x^2 + y^2 = z^2
"""
#x=r+s\,,\,y=r+t\,,\,z=r+s+t.
def factor(val):
    return [(i, int(val / i)) for i in range(1, int(val**0.5)+1) if val % i == 0]
def triplets_from_num(given):
    r = given
    if r % 2 != 0:
        return "number not even"
    r_div = (r**2) / 2
    factors = factor(r_div)
    triplet_to_return = []
    for pair in factors:
        s,t = pair[0],pair[1]
        x = r + s
        y = r + t
        z = r + s + t
        triplet_to_return.append((x,y,z))
    return triplet_to_return

def generate_num_triplets(given):
    found = 0
    triplet_to_return = []
    even_num = 0
    while len(triplet_to_return) < given:
        r = even_num
        r_div = (r**2) / 2
        factors = factor(r_div)
        for pair in factors:
            s,t = pair[0],pair[1]
            x = r + s
            y = r + t
            z = r + s + t
            found = (x,y,z)
            if found in triplet_to_return:
                pass
            else:
                triplet_to_return.append(found)
        even_num += 2
    return triplet_to_return

if __name__ == '__main__':
    todo = input('Would you like to get triplets from your number (enter a) or generate an amount of triplets (enter b)')
    if todo.lower() == 'a':
        num = int(input('Enter an even number : '))
        print(f'Your number would give us the following triplets : {triplets_from_num(num)}')
    elif todo.lower() == 'b':
        amount_to_gen = int(input('How many would you like to generate : '))
        triplets = generate_num_triplets(amount_to_gen)
        print(f'We have found the following triplets from your num\n{triplets}\nThere are {len(triplets)} triplets here')
