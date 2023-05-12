"""Webassets bundles."""
from flask_assets import Bundle
from webassets.filter import get_filter

cookies_js = Bundle(
    "javascripts/utils.js",
    "javascripts/consent.js",
    "javascripts/cookie-banner.js",
    "javascripts/cookies-page.js",
    filters=get_filter(
        "babel",
        binary="node_modules/@babel/cli/bin/babel.js",
        presets="@babel/env",
    ),
    output="cookies.js",
)
