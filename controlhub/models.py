from typing import NotRequired, TypedDict

class ComputerRecord(TypedDict):
    ip: NotRequired[str]
    mac: NotRequired[str]
    name: NotRequired[str]
    data: NotRequired[dict]
    region: NotRequired[str]
    status: NotRequired[str]
    token: NotRequired[str]

class ComputerResponse(ComputerRecord):
    id: str
    updated: str
    created: str

class ExecutionRecord(TypedDict):
    duration: NotRequired[float]
    status: NotRequired[str]
    executable: NotRequired[str]
    logs: NotRequired[str]
    computer: NotRequired[str]
    script: NotRequired[str]
    user: NotRequired[str]
    invisible: NotRequired[bool]

class ExecutionResponse(ExecutionRecord):
    id: str
    updated: str
    created: str
    
class ProcessControlHubPbDataResult(TypedDict):
    server_url: str
    execution_id: str
    computer: ComputerResponse