with open('Desktop\INPUT.txt','r')as f:
    copii=list(f)
a=0
print(f'NR. Nume Prenume Nota1 Nota2 Nota3 ')
with open('Desktop\Rezerva.txt','w') as b:
    for i in copii:
        campuri=i.split()
        print(i)
        b.write(i+'\n')
with open('Destop\Output.txt','w') as c:
    c.write('NR'' '+'Nume '+'Prenume '+'Nota1 '+'Nota2 '+'Nota3 '+'Media '+'\n')
    for i in copii:
        nota=i.split()
        y=nota[0]+' '+nota[1]+' ' +nota[2]
        media=str(float(nota[3])+float(nota[4])+float(nota[5]))
        x=y+''+media+'\n'
    with open('Desktop\Output.txt','a') as c:
            c.write(x)\
with open('Desktop\Output.txt','r') as f:
list3=f.readlines()

