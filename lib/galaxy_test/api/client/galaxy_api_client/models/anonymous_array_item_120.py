from typing import TypeAlias

from .concrete_object_store_model import ConcreteObjectStoreModel
from .user_concrete_object_store_model import UserConcreteObjectStoreModel

__all__ = ["AnonymousArrayItem120"]

AnonymousArrayItem120: TypeAlias = ConcreteObjectStoreModel | UserConcreteObjectStoreModel
