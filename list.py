dostan = ["ali" , "sepehr" , 3 ]
'''print(type(dostan))
print(dostan[2])
print(len(dostan))
# metod len baraye shomaresh item haye daron list hastesh

hack = dostan[:3]
# to khat bala omadim az to list ye list jadid sakhtim
print(hack)
print(dostan[2:5])
# khat bala baramon print mikone az index 2 ta yeki mande be 5
print(dostan[2:])
print(dostan[-3:-1])
# manfi baaks hastesh ghablan gofte shode
print(type(dostan[1:4]))'''


'''print(dostan)

# hala mikhaym yad begirim item ezafe konim ya hazf konim 
dostan[2] = "amir"
print(dostan)'''

'''dostan[2:4] = ["amir" , "reza"]
print(dostan)'''

dostan[1] = ["medi" , "soli"]   
print(dostan)
# ma nemikhaym ye list to list bashe pas myaym mesl paiin amal mikonim
dostan[1:2] = ["medi" , "soli"]   
print(dostan)
# hala mikhaym 1 item ro jaye 2 item bezarim 
dostan[1:4] = ["milad"]   
print(dostan)