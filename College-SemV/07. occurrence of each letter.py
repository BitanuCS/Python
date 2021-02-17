
#Count the occurrence of each letter in "Maharaja Manindra Chandra College".

str = 'Maharaja Manindra Chandra College'

freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequencies of {} is:\n {}".format(str,freq))
