#Use case 1
adj=[]
EDGE=1 #g cost of edge, 
n_nodes = 10
#heuristic costs
cost=[None,0,6,12,9,5,7,1,4,4,1]
children = {1:[2,3,4], 2:[5,6], 3:[7], 4:[8,9], 5:[10]}

#and edges - 1- (2,3), 4-(8,9)


#use case 2
EDGE=5 #g cost of edge, 
adj=[]
n_nodes = 21
#heuristic costs
cost=[None,0,40,2,4,1,2,3,50,60,70,80,4,5,8,9,6,7,90,90,90,90]
children = {1:[2,3,4], 2:[5,6,7], 3:[8,9], 4:[10,11], 5:[12,13], 6:[14,15], 
           7:[16,17], 8:[18], 9:[19], 10:[20], 11:[21] }
#and edges - 1 - (3,4), 2-(5,6,7)
