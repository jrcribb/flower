"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import flwr.proto.node_pb2
import flwr.proto.task_pb2
import flwr.proto.transport_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CreateRunRequest(google.protobuf.message.Message):
    """CreateRun"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class OverrideConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> flwr.proto.transport_pb2.Scalar: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[flwr.proto.transport_pb2.Scalar] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    FAB_ID_FIELD_NUMBER: builtins.int
    FAB_VERSION_FIELD_NUMBER: builtins.int
    OVERRIDE_CONFIG_FIELD_NUMBER: builtins.int
    fab_id: typing.Text
    fab_version: typing.Text
    @property
    def override_config(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, flwr.proto.transport_pb2.Scalar]: ...
    def __init__(self,
        *,
        fab_id: typing.Text = ...,
        fab_version: typing.Text = ...,
        override_config: typing.Optional[typing.Mapping[typing.Text, flwr.proto.transport_pb2.Scalar]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fab_id",b"fab_id","fab_version",b"fab_version","override_config",b"override_config"]) -> None: ...
global___CreateRunRequest = CreateRunRequest

class CreateRunResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___CreateRunResponse = CreateRunResponse

class GetNodesRequest(google.protobuf.message.Message):
    """GetNodes messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RUN_ID_FIELD_NUMBER: builtins.int
    run_id: builtins.int
    def __init__(self,
        *,
        run_id: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["run_id",b"run_id"]) -> None: ...
global___GetNodesRequest = GetNodesRequest

class GetNodesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODES_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.node_pb2.Node]: ...
    def __init__(self,
        *,
        nodes: typing.Optional[typing.Iterable[flwr.proto.node_pb2.Node]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nodes",b"nodes"]) -> None: ...
global___GetNodesResponse = GetNodesResponse

class PushTaskInsRequest(google.protobuf.message.Message):
    """PushTaskIns messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_INS_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_ins_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskIns]: ...
    def __init__(self,
        *,
        task_ins_list: typing.Optional[typing.Iterable[flwr.proto.task_pb2.TaskIns]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ins_list",b"task_ins_list"]) -> None: ...
global___PushTaskInsRequest = PushTaskInsRequest

class PushTaskInsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        task_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_ids",b"task_ids"]) -> None: ...
global___PushTaskInsResponse = PushTaskInsResponse

class PullTaskResRequest(google.protobuf.message.Message):
    """PullTaskRes messages"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_FIELD_NUMBER: builtins.int
    TASK_IDS_FIELD_NUMBER: builtins.int
    @property
    def node(self) -> flwr.proto.node_pb2.Node: ...
    @property
    def task_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        node: typing.Optional[flwr.proto.node_pb2.Node] = ...,
        task_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["node",b"node"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["node",b"node","task_ids",b"task_ids"]) -> None: ...
global___PullTaskResRequest = PullTaskResRequest

class PullTaskResResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TASK_RES_LIST_FIELD_NUMBER: builtins.int
    @property
    def task_res_list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[flwr.proto.task_pb2.TaskRes]: ...
    def __init__(self,
        *,
        task_res_list: typing.Optional[typing.Iterable[flwr.proto.task_pb2.TaskRes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_res_list",b"task_res_list"]) -> None: ...
global___PullTaskResResponse = PullTaskResResponse
