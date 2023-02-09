import datetime


def logger_1(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.datetime.now().strftime("%H:%M:%S")
        name_function = old_function
        arguments = "args ={}, kwargs={}".format(args, kwargs)
        result = old_function(*args, **kwargs)
        dictionary = {
            "name_function": name_function,
            "call_time": call_time,
            "arguments": arguments,
            "result": result,
        }

        with open("main.log", "a", encoding="utf-8") as file:
            file.write(str(dictionary))

        return result

    return new_function


def logger_2(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.datetime.now().strftime("%H:%M:%S")
            name_function = old_function
            arguments = "args ={}, kwargs={}".format(args, kwargs)
            result = old_function(*args, **kwargs)
            dictionary = {
                "name_function": name_function,
                "call_time": call_time,
                "arguments": arguments,
                "result": result,
            }

            with open(path, "a", encoding="utf-8") as file:
                file.write(str(dictionary))
            return result

        return new_function

    return __logger
