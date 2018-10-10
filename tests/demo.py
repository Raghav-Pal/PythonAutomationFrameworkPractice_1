import moment


def func_name(request):
    testname = request.node.name
    print(testname)
    x = moment.now().strftime("%H-%M-%S_%m-%d-%Y")
    # x = moment.date("%H-%M-%S_%m-%d-%Y")
    print(x)

func_name("a")

