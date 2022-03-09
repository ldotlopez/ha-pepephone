import argparse

from . import PepeAPI, RequestError
from pprint import pprint as pp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", required=True)
    parser.add_argument("-p", "--password", required=True)
    parser.add_argument("-n", "--number", required=True)

    args = parser.parse_args()

    api = PepeAPI()
    try:
        api.login(args.username, args.password)
        print(repr(api.get_data(args.number)))
    except RequestError as e:
        pp(e.kwargs["response"].content)
