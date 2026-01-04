from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceRequirement")


@_attrs_define
class ResourceRequirement:
    """
    Attributes:
        type_ (Literal['resource']):
        cores_max (float | int | None | Unset): Maximum reserved number of CPU cores.
            May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs.
            For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means
            that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3).
            The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the
            cores request to the next whole number.
        cores_min (float | int | None | Unset): Minimum reserved number of CPU cores.
            May be a fractional value to indicate to a scheduling algorithm that one core can be allocated to multiple jobs.
            For example, a value of 0.25 indicates that up to 4 jobs may run in parallel on 1 core. A value of 1.25 means
            that up to 3 jobs can run on a 4 core system (4/1.25 ≈ 3).
            The reported number of CPU cores reserved for the process is a non-zero integer calculated by rounding up the
            cores request to the next whole number.
             Default: 1.
        cuda_compute_capability (float | int | None | Unset):
        cuda_device_count_max (float | int | None | Unset):
        cuda_device_count_min (float | int | None | Unset):
        cuda_version_min (float | int | None | Unset):
        gpu_memory_min (float | int | None | Unset):
        ram_max (float | int | None | Unset): Maximum reserved RAM in mebibytes (2**20).
            May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported
            amount of RAM reserved for the process is a non-zero integer.
        ram_min (float | int | None | Unset): Minimum reserved RAM in mebibytes (2**20).
            May be a fractional value. If so, the actual RAM request is rounded up to the next whole number. The reported
            amount of RAM reserved for the process is a non-zero integer. Default: 256.
        shm_size (float | int | None | Unset):
        tmpdir_max (float | int | None | Unset):
        tmpdir_min (float | int | None | Unset):
    """

    type_: Literal["resource"]
    cores_max: float | int | None | Unset = UNSET
    cores_min: float | int | None | Unset = 1
    cuda_compute_capability: float | int | None | Unset = UNSET
    cuda_device_count_max: float | int | None | Unset = UNSET
    cuda_device_count_min: float | int | None | Unset = UNSET
    cuda_version_min: float | int | None | Unset = UNSET
    gpu_memory_min: float | int | None | Unset = UNSET
    ram_max: float | int | None | Unset = UNSET
    ram_min: float | int | None | Unset = 256
    shm_size: float | int | None | Unset = UNSET
    tmpdir_max: float | int | None | Unset = UNSET
    tmpdir_min: float | int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        cores_max: float | int | None | Unset
        if isinstance(self.cores_max, Unset):
            cores_max = UNSET
        else:
            cores_max = self.cores_max

        cores_min: float | int | None | Unset
        if isinstance(self.cores_min, Unset):
            cores_min = UNSET
        else:
            cores_min = self.cores_min

        cuda_compute_capability: float | int | None | Unset
        if isinstance(self.cuda_compute_capability, Unset):
            cuda_compute_capability = UNSET
        else:
            cuda_compute_capability = self.cuda_compute_capability

        cuda_device_count_max: float | int | None | Unset
        if isinstance(self.cuda_device_count_max, Unset):
            cuda_device_count_max = UNSET
        else:
            cuda_device_count_max = self.cuda_device_count_max

        cuda_device_count_min: float | int | None | Unset
        if isinstance(self.cuda_device_count_min, Unset):
            cuda_device_count_min = UNSET
        else:
            cuda_device_count_min = self.cuda_device_count_min

        cuda_version_min: float | int | None | Unset
        if isinstance(self.cuda_version_min, Unset):
            cuda_version_min = UNSET
        else:
            cuda_version_min = self.cuda_version_min

        gpu_memory_min: float | int | None | Unset
        if isinstance(self.gpu_memory_min, Unset):
            gpu_memory_min = UNSET
        else:
            gpu_memory_min = self.gpu_memory_min

        ram_max: float | int | None | Unset
        if isinstance(self.ram_max, Unset):
            ram_max = UNSET
        else:
            ram_max = self.ram_max

        ram_min: float | int | None | Unset
        if isinstance(self.ram_min, Unset):
            ram_min = UNSET
        else:
            ram_min = self.ram_min

        shm_size: float | int | None | Unset
        if isinstance(self.shm_size, Unset):
            shm_size = UNSET
        else:
            shm_size = self.shm_size

        tmpdir_max: float | int | None | Unset
        if isinstance(self.tmpdir_max, Unset):
            tmpdir_max = UNSET
        else:
            tmpdir_max = self.tmpdir_max

        tmpdir_min: float | int | None | Unset
        if isinstance(self.tmpdir_min, Unset):
            tmpdir_min = UNSET
        else:
            tmpdir_min = self.tmpdir_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if cores_max is not UNSET:
            field_dict["cores_max"] = cores_max
        if cores_min is not UNSET:
            field_dict["cores_min"] = cores_min
        if cuda_compute_capability is not UNSET:
            field_dict["cuda_compute_capability"] = cuda_compute_capability
        if cuda_device_count_max is not UNSET:
            field_dict["cuda_device_count_max"] = cuda_device_count_max
        if cuda_device_count_min is not UNSET:
            field_dict["cuda_device_count_min"] = cuda_device_count_min
        if cuda_version_min is not UNSET:
            field_dict["cuda_version_min"] = cuda_version_min
        if gpu_memory_min is not UNSET:
            field_dict["gpu_memory_min"] = gpu_memory_min
        if ram_max is not UNSET:
            field_dict["ram_max"] = ram_max
        if ram_min is not UNSET:
            field_dict["ram_min"] = ram_min
        if shm_size is not UNSET:
            field_dict["shm_size"] = shm_size
        if tmpdir_max is not UNSET:
            field_dict["tmpdir_max"] = tmpdir_max
        if tmpdir_min is not UNSET:
            field_dict["tmpdir_min"] = tmpdir_min

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["resource"], d.pop("type"))
        if type_ != "resource":
            raise ValueError(f"type must match const 'resource', got '{type_}'")

        def _parse_cores_max(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cores_max = _parse_cores_max(d.pop("cores_max", UNSET))

        def _parse_cores_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cores_min = _parse_cores_min(d.pop("cores_min", UNSET))

        def _parse_cuda_compute_capability(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cuda_compute_capability = _parse_cuda_compute_capability(d.pop("cuda_compute_capability", UNSET))

        def _parse_cuda_device_count_max(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cuda_device_count_max = _parse_cuda_device_count_max(d.pop("cuda_device_count_max", UNSET))

        def _parse_cuda_device_count_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cuda_device_count_min = _parse_cuda_device_count_min(d.pop("cuda_device_count_min", UNSET))

        def _parse_cuda_version_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        cuda_version_min = _parse_cuda_version_min(d.pop("cuda_version_min", UNSET))

        def _parse_gpu_memory_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        gpu_memory_min = _parse_gpu_memory_min(d.pop("gpu_memory_min", UNSET))

        def _parse_ram_max(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        ram_max = _parse_ram_max(d.pop("ram_max", UNSET))

        def _parse_ram_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        ram_min = _parse_ram_min(d.pop("ram_min", UNSET))

        def _parse_shm_size(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        shm_size = _parse_shm_size(d.pop("shm_size", UNSET))

        def _parse_tmpdir_max(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        tmpdir_max = _parse_tmpdir_max(d.pop("tmpdir_max", UNSET))

        def _parse_tmpdir_min(data: object) -> float | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | int | None | Unset, data)

        tmpdir_min = _parse_tmpdir_min(d.pop("tmpdir_min", UNSET))

        resource_requirement = cls(
            type_=type_,
            cores_max=cores_max,
            cores_min=cores_min,
            cuda_compute_capability=cuda_compute_capability,
            cuda_device_count_max=cuda_device_count_max,
            cuda_device_count_min=cuda_device_count_min,
            cuda_version_min=cuda_version_min,
            gpu_memory_min=gpu_memory_min,
            ram_max=ram_max,
            ram_min=ram_min,
            shm_size=shm_size,
            tmpdir_max=tmpdir_max,
            tmpdir_min=tmpdir_min,
        )

        resource_requirement.additional_properties = d
        return resource_requirement

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
