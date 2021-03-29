# Subject.py

RxJS Subject implementation in Python.

```
from subject import Subject

subject = Subject()
subject.next(1)

subject.subscribe(lambda res: print('A: ' + str(res)))
subject.next(2)
# A: 2

subject.pipe(
  lambda n: n + 1,
  lambda n: n * 10
)

subject.next(3)
# A: 40

subject.pipe(lambda n: n + 2).pipe(lambda n: n + 3)
subject.subscribe(lambda res: print('B: ' + str(res)))
subject.next(4)
# A: 55
# B: 55
```