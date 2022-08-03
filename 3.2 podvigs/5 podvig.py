class DigitRetrieve:

    def __call__(self, *args, **kwargs):
        for num in args:
            try:
                return int(num)
            except ValueError:
                return None


ex = DigitRetrieve()
print(ex("56abc"))

