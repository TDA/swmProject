#Usage for the update table function
#qs=update_table("player_attr","player_id","2f516c90-3c4d-44ed-81b4-d13e5221d8d3","country","Australia")
#print (qs)
#cur.execute(qs)

def update_table(table_name,key,key_value,field,field_value):
    query_string="UPDATE "+str(table_name)+" SET "+ str(field) +" = '"+str(field_value)+"' WHERE " +str(key)+ " = '"+str(key_value)+ "'"
    return (query_string)
