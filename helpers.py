from typing import Dict, Any


def get_key_by_value(dict_: Dict, val: Any) -> Any:
    return [i for i in dict_ if dict_[i] == val][0]