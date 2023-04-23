import importlib
from typing import List


def add_object_by_name(db_obj, name: str, items: List[dict]):
    model_name = importlib.import_module(f"src.models")
    object_name = "".join([name_part.capitalize() for name_part in name.split("_")])
    model = getattr(model_name, object_name)
    cache_name_id = {}
    for item in items:
        if f"{name}_id" in item:
            if item[f"{name}_id"] in cache_name_id:
                item[name] = cache_name_id[item[f"{name}_id"]]
            else:
                item[name] = model(db_obj).get_by_id(item[f"{name}_id"])
                cache_name_id[item[f"{name}_id"]] = item[name]
