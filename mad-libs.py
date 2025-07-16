# Story Template:
# Once upon a time, a (adjective) dragon named (name) lived in a (adjective) castle. 
# One day, the dragon woke up and couldn't find his (object). He searched (adverb) everywhere but it was nowhere to be found.
# The dragon decided to ask his friend, a (adjective) (animal), for help. Together they looked under (number) rocks and behind (number) trees. 
# Finally, they found it inside a (adjective) (container) in the kitchen.
# "(Exclamation)!" shouted the dragon. "My (same object from before) was here all along!" 
# He was so (emotion) that he (verb) around the castle (number) times.
# From that day forward, the dragon always kept his (same object) in a (adjective) place so he would never lose it again. 
# And they all lived (adverb) ever after!

print('We are going to play a fill-in the gap game, adding random inputs to our story')
print('Fill in the below inputs to create our amazing story')
print()

dragonDescription = input('input an adjective to describe the dragon: ')
dragonName = input('input a name for the dragon: ')
castleDescription = input('input an adjective to describe the castle: ')
dragonObject = input('input an object, e.g toy: ')
searchDescription = input('input an adverb to describe the search: ')
friendDescription = input("input an adjective to describe the dragon's friend: ")
friendType = input('input the type of animal for friend: ')
rockNumber = int(input('input a number: '))
treeNumber = int(input('input another number: '))
containerDescription = input('input an adjective to describe the container: ')
containerType = input('input a kitchen container: ')
exclamation = input('input an exclamation: ')
emotion = input('input a positive emotion: ')
dragonBehaviour = input('input a action/verb a dragon does based on the emotion: ')
numTimes = int(input('input the number of times the dragon does that action: '))
safePlace = input('input an adjective to describe a safe place: ')
endingAdverb = input('input an adverb to end story: ')

print()
print('='*50)
print('HERE IS YOUR STORY:')
print('='*50)
print()

if dragonDescription and dragonName and castleDescription:
    print('Once upon a time, a', dragonDescription, 'dragon named', dragonName, 'lived in a', castleDescription, 'castle.')
    
    if dragonObject:
        print("One day, the dragon woke up and couldn't find his", dragonObject + '.')
        
        if searchDescription:
            print('He searched', searchDescription, 'everywhere but it was nowhere to be found.')
            
            if friendDescription and friendType:
                print('The dragon decided to ask his friend, a', friendDescription, friendType + ', for help.')
                
                if rockNumber and treeNumber:
                    print('Together they looked under', rockNumber, 'rocks and behind', treeNumber, 'trees.')
                    
                    if containerDescription and containerType:
                        print('Finally, they found it inside a', containerDescription, containerType, 'in the kitchen.')
                    
                    if exclamation:
                        print('"' + exclamation + '!" shouted the dragon.')
                        
                        if dragonObject:
                            print('"My', dragonObject, 'was here all along!"')
                            
                            if emotion and dragonBehaviour and numTimes:
                                print('He was so', emotion, 'that he', dragonBehaviour, 'around the castle', numTimes, 'times.')
                                
                                if dragonObject and safePlace:
                                    print('From that day forward, the dragon always kept his', dragonObject, 'in a', safePlace, 'place so he would never lose it again.')
                                    
                                    if endingAdverb:
                                        print('And they all lived', endingAdverb, 'ever after!')
else:
    print("Input not filled, story can't be generated")

print()
print('DONE!')