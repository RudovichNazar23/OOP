
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.attrs = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __getitem__(self, item):
        return self.attrs[item]

    def __setitem__(self, key, value):
        inds = (0, 1, 2, 3, 4)
        if key in inds:
            self.attrs[key] = value
