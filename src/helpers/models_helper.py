import importlib


def add_object_by_name(db_obj, name, items):
    model_name = importlib.import_module(f"src.models")
    model = getattr(model_name, name.capitalize())
    for item in items:
        if f"{name}_id" in item:
            item[name] = model(db_obj).get_by_id(item[f"{name}_id"])