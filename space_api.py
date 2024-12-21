import requests


def get_space_json(date: str = None):
    param_start = ""
    if date:
        param_start = f"&date={date}"
    appid = "gFLQmaUPg4keRrjcs3IY4OXcWRreGNYVALpbg9ka"
    result = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={appid}{param_start}"
    )
    if result.status_code != 200:
        return {}
    return result.json()


def get_space_info(data):
    if type(data) is list:
        return [list, data]
    return [dict, data]
