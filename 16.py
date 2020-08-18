import pickle
with open('TEXT1.TEXT', 'wb+') as file:
    d = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VII', '9': 'IX', '10': 'X'}
    pickle.dump(d, file)

with open('TEXT1.TEXT', 'rb+') as file:
    e = pickle.load(file)

while True:
    dec = str(int(raw_input('Enter decimal number: ')))
    if dec in e.keys():
        print 'The equivalent roman numeral is', e[dec]
    else:
        print 'The equivalent roman numeral is not stored.' 
