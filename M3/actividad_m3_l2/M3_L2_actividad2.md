```python

a = [5, 1, 4, 9, 0]
b = range(3, 10) + range(20, 23)
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa'. 'elefante']
e = ['a', a, 2*a]

```


● a[2] => 4

● b[9] => N/A

● c[1][2] => 5

● e[0] == e[1] => Falso

● len(c) => 3

● len(c[0]) => 2

● len(e) => 3

● c[-1] => [6, 7]

● c[-1][+1] => 7

● c[2:] + d[2:] => [[6,7], 'jirafa', 'elefante']

● a[3:10] => [9, 0]

● a[3:10:2] => [9]

● d.index('jirafa') => 2

● e[c[0][1]].count(5) => 2

● sorted(a)[2] => 4

● complex(b[0], b[1]) => N/A