kerdes = input("Jön Henrik ma kosarazni? (igen/nem) ")
kerdes1 = input("Jön Hanna ma kosarazni? (igen/nem) ")

if kerdes == "igen" and kerdes1 == "igen":
    print("mind a ketten jönnek kosarazni")

elif kerdes == "nem" and kerdes1 == "nem":
    print("egyikük sem jön kosarazni")

else:
    print("csak az egyikük jön kosarazni")