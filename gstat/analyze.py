import csv
import hashlib


def to_csv(filepath, data):
    with open(filepath, 'w') as csvfile:
        stat = csv.DictWriter(csvfile, fieldnames=data[0].keys())

        stat.writeheader()

        for row in data:
            stat.writerow(row)


class FlowLoader:
    def __init__(self, packets):
        self.__packets = packets
        self.__data = dict()

    def analize(self):
        for packet in self.__packets:
            packet_info = {
                "time": packet.frame_info.time_epoch,
                "src": packet.eth.src,
                "dst": packet.eth.dst,

                "t": packet.goose.t,
                "stNum": packet.goose.stnum,
                "sqNum": packet.goose.sqnum,
                "time_allowed_to_live": packet.goose.timeallowedtolive,
                "length": packet.goose.length,
                "goID": packet.goose.goid,
                "gocbRef": packet.goose.gocbref,
                "datset": packet.goose.datset,
                "confrev": packet.goose.confrev,
                "numDatSetEntries": packet.goose.numdatsetentries,
            }

            # key = self.__hash(packet_info["src"], packet_info["dst"])
            self.__add(packet_info["src"], packet_info)

    def __hash(self, src, dst):
        return hashlib.sha256(f"{src}{dst}".encode('utf-8')).hexdigest()

    def __add(self, key, packet_info):
        try:
            self.__data[key].append(packet_info)
        except KeyError:
            self.__data.update({key: list()})
            self.__data[key].append(packet_info)

    @property
    def data(self):
        return self.__data
