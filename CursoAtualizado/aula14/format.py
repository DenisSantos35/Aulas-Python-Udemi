a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
#string2 = 'a={0} c={2} b={1}'
string3 = 'a={nome2} b= {nome1} c={nome0}'
                        #parametro  argumento parametro argumento  parametro argumento
formato = string3.format(nome0 =     a,        nome1 =   b,         nome2 =   c)
print(formato)

