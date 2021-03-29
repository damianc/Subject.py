class Subject:
  operators = []
  subs = []

  def pipe(self, *ops):
    self.operators.extend(ops)
    return self

  def next(self, value):
    if (len(self.operators)):
      for op in self.operators:
        value = op(value)
    for sub in self.subs:
      sub(value)

  def subscribe(self, fn):
    self.subs.append(fn)
