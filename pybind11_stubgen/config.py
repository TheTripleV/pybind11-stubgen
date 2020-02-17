from pydantic import BaseModel
from typing import Dict, List, Optional

class AttributeConfig(BaseModel):
    ignore: bool = False

class FunctionConfig(BaseModel):
    ignore: bool = False

    types_in_doc: bool = True

    docstring: Optional[str] = None
    extra_docstring: Optional[str] = None

class ClassConfig(BaseModel):
    classes: Dict[str, Optional['ClassConfig']] = {}
    methods: Dict[str, Optional[FunctionConfig]] = {}
    attributes: Dict[str, Optional[AttributeConfig]] = {}

    ignore: bool = False

class ModuleConfig(BaseModel):
    modules: Optional[Dict[str, Optional['ModuleConfig']]] = {}
    classes: Dict[str, Optional[ClassConfig]] = {}
    functions: Dict[str, Optional[FunctionConfig]] = {}
    attributes: Dict[str, Optional[AttributeConfig]] = {}

    ignore: bool = False

class Config(BaseModel):
    modules: Optional[Dict[str, Optional[ModuleConfig]]] = {}

    type_map: Dict[str, str] = {}

    # module_attributes_blacklist: List[str] = []
    # class_attributes_blacklist: List[str] = []
    # class_methods_blacklist: List[str] = []
    # class_baseclass_blacklist: List[str] = []


ModuleConfig.update_forward_refs()
ClassConfig.update_forward_refs()