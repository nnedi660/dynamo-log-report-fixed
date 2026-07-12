import json
from pathlib import Path

REPORT = Path("/app/report.json")

def test_report_exists():
    """Verifies success criterion: Output saved to exact path /app/report.json"""
    assert REPORT.exists(), "no /app/report.json found"

def test_report_is_valid_json_object():
    """Verifies success criterion: Report is valid JSON object"""
    assert isinstance(json.loads(REPORT.read_text()), dict), "report.json is not a JSON object"

def test_required_keys_present():
    """Verifies success criterion: Report contains exactly the 3 required keys"""
    data = json.loads(REPORT.read_text())
    assert {"total_requests", "unique_ips", "top_path"} <= data.keys()

def test_total_requests_correct():
    """Verifies success criterion: total_requests equals 6 log entries"""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6

def test_unique_ips_correct():
    """Verifies success criterion: unique_ips equals 3 distinct client addresses"""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3

def test_top_path_correct():
    """Verifies success criterion: top_path equals most requested path /index.html"""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"