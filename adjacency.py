from numpy import *
import communication_cost as cc
#final_rows = list((('Australia', 'f21ad593-f71a-4c0c-899b-2acef00cc1f2'), ('New Zealand', '966686da-c6a5-4592-bb23-d5d14e205828'), ('Sri Lanka', 'cbfa40b3-bddc-489c-a0cc-c06e68d5f8c7'), ('West Indies', 'b87854a5-36d0-4f8e-a139-deb5ae73de8e'), ('India', '3d7a9401-4c0d-4df3-befa-fb1ce56d4da4'), ('West Indies', '88cf5b9b-e328-4885-a6a2-946685943200'), ('Bangladesh', 'fa9880d7-721b-4d35-b562-5ca58ff1183c'), ('Zimbabwe', 'cd87f314-899e-49f8-b116-4dc13cb5087e'), ('South Africa', '85719016-4c14-48a6-9a26-f9abc69956f0'), ('India', 'd30f2232-9baa-4998-afcc-ca5d4386c992'), ('West Indies', '3a1542f3-b792-429e-b0d0-43db9b7b7cbc'), ('India', 'fb453f22-1887-4cf8-83c1-dca7444fe52d'), ('Sri Lanka', '13b5a6dc-a0a9-4912-a5a9-1cc1cc49d44c'), ('Australia', 'cf560515-1c57-4d6a-a916-db14b2fe9341'), ('Zimbabwe', '1d560671-12f7-406e-8ade-d87e6b2da1bc'), ('Pakistan', '54a30f11-01f5-4642-950e-1754cfed4788'), ('Zimbabwe', '9057716f-75bd-443e-a753-2636cdf3c2fc'), ('Sri Lanka', 'c4e10cce-39fd-4795-85e0-19268f7d0abe'), ('Bangladesh', '409a68cc-7eb3-4c34-9573-1cf44652b7d3'), ('New Zealand', 'd535e4d4-0d2a-4e54-8661-d3c5dd88bbf5'), ('Australia', '1b2655bb-ed06-470c-8288-70ab1c8e5682'), ('Ireland', '185a7c2f-0953-4f35-8208-c50d5b0efd9f'), ('Zimbabwe', 'be0b056f-6090-475e-8d85-5c04b21b13cf'), ('England', '534c67e8-a900-4dfb-8837-99b2e226b7e3'), ('India', 'e5ad2a7b-a684-4b8e-8f89-32991f4f57e0'), ('West Indies', '97d6bf61-bc4d-4ab0-a407-1345dc278408'), ('Sri Lanka', '52b400a1-bec9-44df-ad29-ab0fd5c98f1c'), ('Sri Lanka', '90a3723c-263e-44ca-965a-55f983b88dca'), ('Bangladesh', '1cafe5fe-ba04-4773-bf3b-24cc29688fdd'), ('Afghanistan', '0658275d-e820-42d2-a307-ddea1569ee5a')))

def build_adjacencymatrix(final_rows):
    length_players = len(final_rows)
    adjacency_matrix= zeros(shape=(length_players,length_players),dtype=int)
    for x in final_rows:
        for y in final_rows:
            adjacency_matrix[final_rows.index(x),final_rows.index(y)]=cc.communication_cost[x[0],y[0]]            
    return adjacency_matrix
        
    