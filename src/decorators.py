def validate_attributes(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        ann_vals = list(annotations.values())
        ann_keys = list(annotations.keys())

        for index, arg in enumerate(args):
            if not isinstance(arg, list(annotations.values())[index]):
                raise Exception(f"Wrong type for attribute '{ann_keys[index]}', "
                                f"expected: {ann_vals[index].__name__}, "
                                f"given: {type(arg).__name__}")
        for key, val in kwargs.items():
            if not isinstance(val, annotations[key]):
                raise Exception(f"Wrong type for attribute '{key}', "
                                f"expected: {annotations[key].__name__}, "
                                f"given: {type(val).__name__}")
        ret_value = func(*args, **kwargs)
        if not isinstance(ret_value, annotations["return"]):
            raise Exception(f"Wrong return value type. Expected: {annotations['return'].__name__}, "
                            f"returned {type(ret_value).__name__}")
    return wrapper
