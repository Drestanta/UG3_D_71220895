deret_awal = int(input('masukan awal deret: '))
deret_akhir = int(input('masukan akhir deret: '))
 
for i in range(deret_akhir,deret_awal+1):
  if (i % 2 == 0):
    print(i)