from src.storage import save_state, load_state

def test_state_roundtrip(tmp_path):
    p = tmp_path / "state.json"
    save_state(str(p), [{"id": 1}], version=2)
    st = load_state(str(p))
    assert st["version"] == 2
    assert st["items"] == [{"id": 1}]
