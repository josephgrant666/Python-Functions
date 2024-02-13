# Add a dictionary within a dictionary

x = { 
    'y': {'a':'b','c':'d'
},
    'z': {'e':'f','g':'h'
}
}

data = {
    'i' : 'j',
    'k' : 'l'
}

x['q'] = data # Would add a new dictionary within the dictionary with the key-value pairs that are given by the variable 'data' 