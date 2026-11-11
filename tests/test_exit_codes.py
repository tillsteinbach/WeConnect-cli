"""Unknown ids must fail with exit code 1, not 255 (sys.exit(-1))."""

import sys
from unittest.mock import patch

import pytest

from weconnect import weconnect as wc_mod

import weconnect_cli.weconnect_cli_base as base


class FakeWeConnect:
    def __init__(self, *args, **kwargs):
        pass

    def login(self):
        pass

    def update(self, *args, **kwargs):
        pass

    def getByAddressString(self, _):
        return None

    def persistTokens(self):
        pass

    def persistCacheAsJson(self, _):
        pass

    def disconnect(self):
        pass


def run(argv):
    with patch.object(wc_mod, "WeConnect", FakeWeConnect):
        with patch.object(sys, "argv", argv):
            with pytest.raises(SystemExit) as exc_info:
                base.main()
    return exc_info.value.code


def test_get_unknown_id_exits_1():
    assert run(["weconnect-cli", "-u", "u", "-p", "p", "--no-cache",
                "get", "someid"]) == 1


def test_set_unknown_id_exits_1():
    assert run(["weconnect-cli", "-u", "u", "-p", "p", "--no-cache",
                "set", "someid", "somevalue"]) == 1
