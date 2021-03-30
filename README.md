# Subject.py

RxJS Subject implementation in Python.

```
from subject import Subject

subject = Subject()
subject.next(1)

subject.subscribe(lambda res: print('A: ' + str(res)))
subject.next(2)
# A: 2

subject.subscribe(lambda res: print('B: ' + str(res)))
subject.next(3)
# A: 3
# B: 3
```

## Mappers

```
subject.pipe(
  lambda n: n + 1,
  lambda n: n * 10
)
```

* in chain:

```
subject.pipe(
  lambda n: n + 1
).pipe(
  lambda n: n * 10
)
```

## Caching

* to define how many values are to be cached, use the `cached` named parameter
* to define initial cached values, use the `init` named parameter

```
subject = Subject(cache=2, init=[1, 2])
subject.subscribe(lambda res: print('A: ' + str(res)))
# A: 1
# A: 2

subject.next(3)
# A: 3

subject.subscribe(lambda res: print('B: ' + str(res)))
# B: 2
# B: 3

subject.next(4)
# A: 4
# B: 4
```

## Observers

* function

```
subject.subscribe(lambda res: print(res))
```

* dictionary

```
subject.subscribe({
  'next': lambda res: print(res),
  'error': lambda err: print('ERROR:', err),
  'complete': lambda: print('DONE')
})
```

> All functions in the dictionary are optional.