__all__ = [
    "IRoleRepository",
    "IResourceRepository",
    "IRoleXResourceRepository",
]


from .role import IRoleRepository
from .resource import IResourceRepository
from .role_x_resource import IRoleXResourceRepository
