# Loop over dictionaries

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe. The .items() method helps to do this. 
for k,v in europe.items():
    print(str("the capital of " + k + str(' is ') + v))