a=['','one','two','three','four','five','six','seven','eight','nine']
b={11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
c=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninenty']

e=input('enter a no: ')
f=len(e)
g=int(e)

if f==1:
    h=a[g]
    print(h)
elif f==2:
    if g<20:
        print(b[g])
    elif g>19 and g<100:
        j=g//10
        k=g%10
        print(c[j]+" "+a[k])
elif f==3:
    if g>99 and g<1000:
        u=g%100
        if u>10 and u<20:
            h2 = g//100
            h1 = g % 100
            print(a[h2],'hundred and',b[h1])
        else:
            h2 = g//100
            hh = g % 100
            h1 = hh//10
            h3 = hh % 10
            if e=='100':
                print(a[h2],'hundred')
            else:    
                print(a[h2],'hundred and '+c[h1]+" "+a[h3])