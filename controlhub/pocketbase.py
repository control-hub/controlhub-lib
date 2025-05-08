import os
import requests
import json

from controlhub.models import (
    ComputerRecord,
    ComputerResponse,
    ExecutionRecord,
    ExecutionResponse,
    ProcessControlHubPbDataResult,
)

def process_controlhub_pb_data() -> ProcessControlHubPbDataResult:
    try:
        server_url = os.getenv("CONTROLHUB_SERVER_URL")
        execution_id = os.getenv("EXECUTION_ID")
        computer = json.loads(os.getenv("COMPUTER_JSON"))

        if None in (server_url, execution_id, computer):
            raise NotImplementedError()
    except Exception:
        raise NotImplementedError(
            "Use this function only in controlhub client scripts, or specify env variables `CONTROLHUB_SERVER_URL`, `EXECUTION_ID`, `COMPUTER_JSON`"
        )

    return {
        "server_url": server_url,
        "execution_id": execution_id,
        "computer": computer,
    }


def get_execution() -> ExecutionResponse:
    """
    Returns execution data from controlhub pocketbase db
    """
    processed_data = process_controlhub_pb_data()

    result = requests.get(
        processed_data["server_url"]
        + "/api/collections/executions/records/"
        + processed_data["execution_id"],
        params={"token": processed_data["computer"]["token"]},
    )

    return result.json()


def update_execution(data: ExecutionRecord) -> ExecutionResponse:
    """
    Updates execution in controlhub pocketbase db

    Args:
        data (ExecutionRecord: dict): Changed execution
    """
    processed_data = process_controlhub_pb_data()

    result = requests.patch(
        processed_data["server_url"]
        + "/api/collections/executions/records/"
        + processed_data["execution_id"],
        params={"token": processed_data["computer"]["token"]},
        json=data,
    )
    
    return result.json()


def get_offline_computer() -> ComputerResponse:
    """
    Returns computer data from env
    """
    processed_data = process_controlhub_pb_data()

    return processed_data["computer"]


def get_computer() -> ComputerResponse:
    """
    Returns computer data from controlhub pocketbase db
    """
    processed_data = process_controlhub_pb_data()

    result = requests.get(
        processed_data["server_url"]
        + "/api/collections/computers/records/"
        + processed_data["computer"]["id"],
        params={"token": processed_data["computer"]["token"]},
    )

    return result.json()


def update_computer(data: ComputerRecord) -> ExecutionResponse:
    """
    Updates computer in controlhub pocketbase db

    Args:
        data (ComputerRecord: dict): Changed computer
    """
    processed_data = process_controlhub_pb_data()

    result = requests.patch(
        processed_data["server_url"]
        + "/api/collections/computers/records/"
        + processed_data["computer"]["id"],
        params={"token": processed_data["computer"]["token"]},
        json=data,
    )
    
    return result.json()
