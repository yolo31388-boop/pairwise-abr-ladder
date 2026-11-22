import pytest
import media.abr_ladder as mod

CASES = [
    ("content_bitrate", (1.5, 0.4)),
    ("gop_align", (30, 2.0)),
    ("first_keyframe", (1, 2)),
    ("res_bitrate_match", (1080, 1.0)),
    ("hysteresis_switch", (0.8, 0.9)),
    ("buffer_aware", (1.0, 2.0)),
    ("shared_audio", (1, 2)),
    ("per_rendition_tonemap", (1.0, 0.5)),
    ("concurrency_limit", (4, 2)),
    ("manifest_bandwidth", (2.5, 0.3)),
    ("ladder_sort", ([720, 1080, 480],)),
    ("segment_duration", (2.0, 1.0)),
    ("codec_profile", (1, 2)),
    ("audio_offset", (0.0, 0.5)),
    ("switch_cost", (1.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
