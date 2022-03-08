__all__ = (
    'render_target_url',
)
import random as rand

from time import sleep

import requests_html


RETRY = 10
MIN_PAUSE = 0
MAX_PAUSE = 3

USER_AGENTS = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4464.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
)


def default_validator(html):
    """Returns True if html contains valid data"""
    return True


def get_user_agent():
    """Return a random user agent"""
    return rand.choice(USER_AGENTS)


def render_target_url(
    url, ss=None, headers=None, is_js=False,
    validator=default_validator, retry=RETRY,
    min_pause=MIN_PAUSE, max_pause=MAX_PAUSE
):
    """Generate HTML object from the given URL"""
    ss = ss or requests_html.HTMLSession()
    _headers = {
        'User-Agent': get_user_agent(),
    }
    _headers.update(headers or {})

    def _exec():
        res = ss.get(url, headers=_headers)
        res.raise_for_status()
        if is_js:
            res.html.render()
        return res.html

    html = _exec()
    runs = 0
    while not validator(html) and runs < retry:
        html = _exec()
        runs += 1
        sleep(rand.randrange(min_pause, max_pause))

    if not validator(html):
        raise ValueError(f'Failed to find valid data after {retry} retries!')

    return html
