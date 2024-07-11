#!/usr/bin/env python
# -*- coding: utf-8 -*-


from instrument_response.instrument_response import InstrumentResponse
from pkg_resources import get_distribution

__version__ = get_distribution("instrument-response").version
__author__ = "Martanto"
__author_email__ = "martanto@live.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2024, MAGMA Indonesia"
__url__ = "https://github.com/martanto/instrument-response"

__all__ = [
    "InstrumentResponse",
]