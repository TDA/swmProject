#!C:\Python27\python2.7.exe
def return_players(adj_mat,rank_list,no_of_players):
	minimum=1000
	highest_rank=1
	first_player_index=0
	second_player_index=0
	selected_players=list()
	for i in range(0,len(adj_mat)):
		#print i
		for j in range(0,len(adj_mat)):
			if(( i != j ) and ((adj_mat[i][j]<=minimum) and rank_list[i]>=highest_rank)):
				minimum=adj_mat[i][j]
				highest_rank=rank_list[i]
				#print minimum
				#print i,j, highest_rank
				first_player_index=i
				second_player_index=j
	#print first_player_index,second_player_index
	selected_players.append(first_player_index)
	selected_players.append(second_player_index)
	nullify(adj_mat,first_player_index,second_player_index)
	for x in selected_players:
		new_player=return_least_index(adj_mat,x)
		if(len(selected_players)==no_of_players):
			break
		else:
			selected_players.append(new_player)

	print selected_players
			#print adj_mat[i][j]
	print no_of_players

def return_least_index(row,index):
	mini=1000
	least_index=0
	for i in range(0,len(row[index])):

		if((index!=i) and (row[index][i]<=mini)):
			#print i,index,row[index][i]
			mini=row[index][i]
			least_index=i
	#print least_index
	nullify(row,index,least_index)
	return  least_index

def nullify(adj_mat,i,j):
	adj_mat[i][j]=1001
	adj_mat[i][i]=1001
	adj_mat[j][j]=1001
	adj_mat[j][i]=1001
	#return adj_mat


wicket_keepers=[[0,30,17,1,11,42],
 [30,0,88,20,26,41],
 [17,88,0,34,35,10],
 [1,20,34,0,82,2],
 [11,26,35,82,0,80],
 [42,41,10,2,80,0]]

ranks=[34,55,66,87,35,99]
return_players(wicket_keepers,ranks,3)