my_num=7
num=None
while my_num!=num:
    num = int(input('1-9 arasi texmin etdiyiniz reqem?:'))
    if not 0<num<10:
        print('reqem araliqdan kenardadir.')
        exit()
    elif num==my_num:
        print('tebrikler!!!')   
    else:
        print('dogru tapmadiniz')      

