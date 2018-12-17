#!/usr/bin/env python3.7
import argparse
import csv
import uuid

import pyshark

from gstat import analyze


def to_csv(filepath, data):
    with open(filepath, 'w') as csvfile:
        stat = csv.DictWriter(csvfile, fieldnames=data[0].keys())

        for row in data:
            stat.writerow(row)


def main():
    command_line = argparse.ArgumentParser(
        prog='gstat',
        description='The goose_stat script analyzes packets of goose protocol. '
                    'It writes results into csv files of specified directory.')

    command_line.add_argument(
        '-i', '--input', help='pcap file', required=True)
    command_line.add_argument(
        '-d', '--dir', help="directory were results would be stored", required=True)

    args = command_line.parse_args()

    pcap_file = pyshark.FileCapture(args.input)

    flow_loader = analyze.FlowLoader(pcap_file)
    flow_loader.analize()

    for data in flow_loader.data.values():
        to_csv(f"{uuid.uuid4()}.csv", data)


if __name__ == '__main__':
    main()
