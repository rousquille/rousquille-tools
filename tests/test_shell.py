from rousquille_tools.shell import is_in_screen_session


def test_is_not_in_screen_session():
    assert not is_in_screen_session()
