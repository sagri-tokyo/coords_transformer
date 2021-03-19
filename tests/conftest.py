import importlib
import sys
import os
import pytest
from src.constants import ZOOM
from src import coords_transformer
from src.point import Point


#  Values used as parameters are on the below site.
#  https://www.trail-note.net/tech/coordinate/
SAMPLE_POINTS = [
    Point(x=29941927, y=12046802, lng=141.242035, lat=45.178506),
    Point(x=29727726, y=13192979, lng=138.943905, lat=35.855499),
    Point(x=28941096, y=13807510, lng=130.504283, lat=30.335927),
]

@pytest.fixture(scope="session")
def monkeypatch():
    from _pytest.monkeypatch import MonkeyPatch
    monkeypatch = MonkeyPatch()
    return monkeypatch

@pytest.fixture(scope="module")
def setup_zoom(monkeypatch):
    monkeypatch.setattr("src.constants.ZOOM", 17)
    importlib.reload(coords_transformer)
    yield
    monkeypatch.setattr("src.constants.ZOOM", ZOOM)

@pytest.fixture(params=SAMPLE_POINTS, scope="function")
def sample_point(request):
    return request.param
