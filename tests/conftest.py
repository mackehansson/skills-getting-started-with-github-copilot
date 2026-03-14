"""Shared pytest fixtures for backend API tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities before and after every test."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app_module.app)
