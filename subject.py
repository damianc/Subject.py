class Subject:
  operators = []
  subs = []
  cachedItems = []
  cachedNum = 0
  completed = False

  '''
  __init__
  '''
  def __init__(self, *, cached = 0, init = []):
    if (cached > 0):
      self.cachedNum = cached
      if (len(init)):
        self.cachedItems = [*init[-cached:]]

  '''
  pipe
  '''
  def pipe(self, *ops):
    self.operators.extend(ops)
    return self

  '''
  next
  '''
  def next(self, value):
    if self.completed:
      return

    self.__putInCache(value)
    value = self.__applyOperators(value)

    for sub in self.subs:
      if isinstance(sub, type({})):
        if 'next' in sub:
          sub['next'](value)
      else:
        sub(value)

  '''
  complete
  '''
  def complete(self):
    if self.completed:
      return

    self.completed = True
    for sub in self.subs:
      if isinstance(sub, type({})):
        if 'complete' in sub:
          sub['complete']()

  '''
  error
  '''
  def error(self, message):
    if self.completed:
      return

    errorHandlers = 0

    for sub in self.subs:
      if isinstance(sub, type({})):
        if 'error' in sub:
          errorHandlers += 1
          sub['error'](message)

    if (errorHandlers == 0):
      raise Exception(message)

  '''
  subscribe
  '''
  def subscribe(self, fn):
    self.subs.append(fn)

    if (self.cachedNum > 0 and len(self.cachedItems)):
      for cachedVal in self.cachedItems:
        self.next(cachedVal)

  '''
  __applyOperators
  '''
  def __applyOperators(self, value):
    if (len(self.operators)):
      for op in self.operators:
        value = op(value)

    return value

  '''
  __putInCache
  '''
  def __putInCache(self, value):
    if (len(self.cachedItems) < self.cachedNum):
      self.cachedItems.append(value)
    else:
      self.cachedItems = self.cachedItems[1:] + [value]