import os

# bearer_token = os.environ.get("BEARER_TOKEN")
# print(bearer_token)
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGAkigEAAAAApKiVyFfDRYeJphU49dUfqC3e2cY%3Dmnkb2oCZBr7VdsuMBZzOGR9OMWtOnD3pS2Ap9bKjeixAWo7HfO'

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r
