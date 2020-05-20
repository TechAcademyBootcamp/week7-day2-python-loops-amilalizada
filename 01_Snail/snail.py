heigth = int(input('qet edilesi hundurluk?:'))
move = int(input('gundelik qet edilen mesafe?:'))
cut = int(input('gundelik surushduyu mesafe?:'))
daily_net =0
net=0
iterator=0
while net <= heigth:   
    daily_net = move-cut
    net += daily_net
    iterator+=1
    
print(iterator-1)
