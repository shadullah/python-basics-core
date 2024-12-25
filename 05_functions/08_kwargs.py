# def print_kwargs(name, power):
    # print("name ", name, "po/wer ", power)
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shktiman", power="laser")
print_kwargs(name="shktiman", power="laser",gali="vega")