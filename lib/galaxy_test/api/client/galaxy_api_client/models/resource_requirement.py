from dataclasses import dataclass

from .resource_requirement_cores_max import ResourceRequirementCoresMax
from .resource_requirement_cores_min import ResourceRequirementCoresMin
from .resource_requirement_cuda_compute_capability import ResourceRequirementCudaComputeCapability
from .resource_requirement_cuda_device_count_max import ResourceRequirementCudaDeviceCountMax
from .resource_requirement_cuda_device_count_min import ResourceRequirementCudaDeviceCountMin
from .resource_requirement_cuda_version_min import ResourceRequirementCudaVersionMin
from .resource_requirement_gpu_memory_min import ResourceRequirementGpuMemoryMin
from .resource_requirement_ram_max import ResourceRequirementRamMax
from .resource_requirement_ram_min import ResourceRequirementRamMin
from .resource_requirement_shm_size import ResourceRequirementShmSize
from .resource_requirement_tmpdir_max import ResourceRequirementTmpdirMax
from .resource_requirement_tmpdir_min import ResourceRequirementTmpdirMin

__all__ = ["ResourceRequirement"]


@dataclass
class ResourceRequirement:
    """
    ResourceRequirement dataclass

    Args:
        type_ (str)              : Maps from 'type'
        cores_max (ResourceRequirementCoresMax | None)
                                 : Maximum reserved number of CPU cores. May be a fractional
                                   value to indicate to a scheduling algorithm that one core
                                   can be allocated to multiple jobs. For example, a value
                                   of 0.25 indicates that up to 4 jobs may run in parallel
                                   on 1 core. A value of 1.25 means that up to 3 jobs can
                                   run on a 4 core system (4/1.25 ≈ 3). The reported number
                                   of CPU cores reserved for the process is a non-zero
                                   integer calculated by rounding up the cores request to
                                   the next whole number.
        cores_min (ResourceRequirementCoresMin | None)
                                 : Minimum reserved number of CPU cores. May be a fractional
                                   value to indicate to a scheduling algorithm that one core
                                   can be allocated to multiple jobs. For example, a value
                                   of 0.25 indicates that up to 4 jobs may run in parallel
                                   on 1 core. A value of 1.25 means that up to 3 jobs can
                                   run on a 4 core system (4/1.25 ≈ 3). The reported number
                                   of CPU cores reserved for the process is a non-zero
                                   integer calculated by rounding up the cores request to
                                   the next whole number.
        cuda_compute_capability (ResourceRequirementCudaComputeCapability | None)
                                 :
        cuda_device_count_max (ResourceRequirementCudaDeviceCountMax | None)
                                 :
        cuda_device_count_min (ResourceRequirementCudaDeviceCountMin | None)
                                 :
        cuda_version_min (ResourceRequirementCudaVersionMin | None)
                                 :
        gpu_memory_min (ResourceRequirementGpuMemoryMin | None)
                                 :
        ram_max (ResourceRequirementRamMax | None)
                                 : Maximum reserved RAM in mebibytes (2**20). May be a
                                   fractional value. If so, the actual RAM request is
                                   rounded up to the next whole number. The reported amount
                                   of RAM reserved for the process is a non-zero integer.
        ram_min (ResourceRequirementRamMin | None)
                                 : Minimum reserved RAM in mebibytes (2**20). May be a
                                   fractional value. If so, the actual RAM request is
                                   rounded up to the next whole number. The reported amount
                                   of RAM reserved for the process is a non-zero integer.
        shm_size (ResourceRequirementShmSize | None)
                                 :
        tmpdir_max (ResourceRequirementTmpdirMax | None)
                                 :
        tmpdir_min (ResourceRequirementTmpdirMin | None)
                                 :
    """

    type_: str  # Maps from 'type'
    cores_max: ResourceRequirementCoresMax | None = (
        None  # Maximum reserved number of CPU cores. May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3). The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.
    )
    cores_min: ResourceRequirementCoresMin | None = (
        1  # Minimum reserved number of CPU cores. May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3). The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.
    )
    cuda_compute_capability: ResourceRequirementCudaComputeCapability | None = None
    cuda_device_count_max: ResourceRequirementCudaDeviceCountMax | None = None
    cuda_device_count_min: ResourceRequirementCudaDeviceCountMin | None = None
    cuda_version_min: ResourceRequirementCudaVersionMin | None = None
    gpu_memory_min: ResourceRequirementGpuMemoryMin | None = None
    ram_max: ResourceRequirementRamMax | None = (
        None  # Maximum reserved RAM in mebibytes (2**20). May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.
    )
    ram_min: ResourceRequirementRamMin | None = (
        256  # Minimum reserved RAM in mebibytes (2**20). May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.
    )
    shm_size: ResourceRequirementShmSize | None = None
    tmpdir_max: ResourceRequirementTmpdirMax | None = None
    tmpdir_min: ResourceRequirementTmpdirMin | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "cores_max": "cores_max",
            "cores_min": "cores_min",
            "cuda_compute_capability": "cuda_compute_capability",
            "cuda_device_count_max": "cuda_device_count_max",
            "cuda_device_count_min": "cuda_device_count_min",
            "cuda_version_min": "cuda_version_min",
            "gpu_memory_min": "gpu_memory_min",
            "ram_max": "ram_max",
            "ram_min": "ram_min",
            "shm_size": "shm_size",
            "tmpdir_max": "tmpdir_max",
            "tmpdir_min": "tmpdir_min",
            "type": "type_",
        }
        key_transform_with_dump = {
            "cores_max": "cores_max",
            "cores_min": "cores_min",
            "cuda_compute_capability": "cuda_compute_capability",
            "cuda_device_count_max": "cuda_device_count_max",
            "cuda_device_count_min": "cuda_device_count_min",
            "cuda_version_min": "cuda_version_min",
            "gpu_memory_min": "gpu_memory_min",
            "ram_max": "ram_max",
            "ram_min": "ram_min",
            "shm_size": "shm_size",
            "tmpdir_max": "tmpdir_max",
            "tmpdir_min": "tmpdir_min",
            "type_": "type",
        }
