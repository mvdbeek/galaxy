from typing import TypeAlias

from .concrete_object_store_model import ConcreteObjectStoreModel
from .user_concrete_object_store_model import UserConcreteObjectStoreModel

__all__ = ["AnonymousArrayItem121"]

AnonymousArrayItem121: TypeAlias = ConcreteObjectStoreModel | UserConcreteObjectStoreModel
