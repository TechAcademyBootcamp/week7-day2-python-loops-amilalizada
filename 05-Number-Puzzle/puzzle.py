print('Program haqqinda melumat...')
array=[]
number = input('eded daxil edin: ')
while not number.isdigit() or int(number)<0:
    number=input('eded musbet olmalidir.')
divider = input('nece hisseye bolmek isteirsiniz?')
while not divider.isdigit() or int(divider)<0 or len(number)%int(divider)!=0:
    print('sehvlik bash verdi .nece hisseye bolmek isteirsiniz?')
divider=int(divider)
divided = len(number)//divider
for i in range(divided):


