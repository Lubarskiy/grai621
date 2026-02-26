from src.parsers import parse_kv_pairs

def test_parse_kv_pairs():
    assert parse_kv_pairs("a=1;b=2") == {"a": "1", "b": "2"}
