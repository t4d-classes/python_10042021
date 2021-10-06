from typing import Any, Callable

def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
        print("start")
        return fn(*args, **kwargs) # do_it invoked
    return inner

def do_it(a: int, b: int) -> int:
    return a + b

# print(do_it(1,2))

# func_a = wrapper(do_it) # return inner function
# print(func_a(1,2))

@wrapper
def do_it2(a: int, b: int) -> int:
    return a + b

@wrapper
def do_it3(a: int, b: int, c: int) -> int:
    return a + b + c

print(do_it2(1,2))
print(do_it3(1,c=2,b=3))