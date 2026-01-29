from dataclasses import dataclass

from .cores_max import CoresMax
from .cores_min import CoresMin
from .cuda_compute_capability import CudaComputeCapability
from .cuda_device_count_max import CudaDeviceCountMax
from .cuda_device_count_min import CudaDeviceCountMin
from .cuda_version_min import CudaVersionMin
from .gpu_memory_min import GpuMemoryMin
from .ram_max import RamMax
from .ram_min import RamMin
from .shm_size import ShmSize
from .tmpdir_max import TmpdirMax
from .tmpdir_min import TmpdirMin

__all__ = ["ResourceRequirement"]


@dataclass
class ResourceRequirement:
    """
    ResourceRequirement dataclass.

    Args:
        type_ (str)              :
        cores_max (Optional[CoresMax])
                                 : Maximum reserved number of CPU cores. May be a fractional
                                   value to indicate to a scheduling algorithm that one core
                                   can be allocated to multiple jobs. For example, a value
                                   of 0.25 indicates that up to 4 jobs may run in parallel
                                   on 1 core. A value of 1.25 means that up to 3 jobs can
                                   run on a 4 core system (4/1.25 ≈ 3). The reported number
                                   of CPU cores reserved for the process is a non-zero
                                   integer calculated by rounding up the cores request to
                                   the next whole number.
        cores_min (Optional[CoresMin])
                                 : Minimum reserved number of CPU cores. May be a fractional
                                   value to indicate to a scheduling algorithm that one core
                                   can be allocated to multiple jobs. For example, a value
                                   of 0.25 indicates that up to 4 jobs may run in parallel
                                   on 1 core. A value of 1.25 means that up to 3 jobs can
                                   run on a 4 core system (4/1.25 ≈ 3). The reported number
                                   of CPU cores reserved for the process is a non-zero
                                   integer calculated by rounding up the cores request to
                                   the next whole number.
        cuda_compute_capability (Optional[CudaComputeCapability])
                                 :
        cuda_device_count_max (Optional[CudaDeviceCountMax])
                                 :
        cuda_device_count_min (Optional[CudaDeviceCountMin])
                                 :
        cuda_version_min (Optional[CudaVersionMin])
                                 :
        gpu_memory_min (Optional[GpuMemoryMin])
                                 :
        ram_max (Optional[RamMax]): Maximum reserved RAM in mebibytes (2**20). May be a
                                    fractional value. If so, the actual RAM request is
                                    rounded up to the next whole number. The reported amount
                                    of RAM reserved for the process is a non-zero integer.
        ram_min (Optional[RamMin]): Minimum reserved RAM in mebibytes (2**20). May be a
                                    fractional value. If so, the actual RAM request is
                                    rounded up to the next whole number. The reported amount
                                    of RAM reserved for the process is a non-zero integer.
        shm_size (Optional[ShmSize])
                                 :
        tmpdir_max (Optional[TmpdirMax])
                                 :
        tmpdir_min (Optional[TmpdirMin])
                                 :
    """

    type_: str
    cores_max: CoresMax | None = (
        None  # Maximum reserved number of CPU cores. May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3). The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.
    )
    cores_min: CoresMin | None = (
        1  # Minimum reserved number of CPU cores. May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs. For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3). The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the cores request to the next whole number.
    )
    cuda_compute_capability: CudaComputeCapability | None = None
    cuda_device_count_max: CudaDeviceCountMax | None = None
    cuda_device_count_min: CudaDeviceCountMin | None = None
    cuda_version_min: CudaVersionMin | None = None
    gpu_memory_min: GpuMemoryMin | None = None
    ram_max: RamMax | None = (
        None  # Maximum reserved RAM in mebibytes (2**20). May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.
    )
    ram_min: RamMin | None = (
        256  # Minimum reserved RAM in mebibytes (2**20). May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported amount of RAM reserved for the process is a non-zero integer.
    )
    shm_size: ShmSize | None = None
    tmpdir_max: TmpdirMax | None = None
    tmpdir_min: TmpdirMin | None = None
