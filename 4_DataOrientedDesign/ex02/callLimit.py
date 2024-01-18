def callLimit(limit: int):
    """def callLimit(limit: int)"""
    count = 0

    def callLimiter(function):
        """def callLimiter(function)"""
        def limit_function(*args: any, **kwds: any):
            """def limit_function(*args: any, **kwds: any)"""
            nonlocal count
            if (count >= limit):
                print(f"Error: {function} call too many times")
                return (None)
            count += 1
            return (function(*args, **kwds))
        return (limit_function)
    return (callLimiter)


if __name__ == "__main__":
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()
