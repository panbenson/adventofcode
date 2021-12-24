# https://adventofcode.com/2021/day/16
import read_input
import heapq
from collections import defaultdict
from collections import deque


def parse_packet(bin_str):
    print('looking at bin_str:', bin_str)
    packet_version = int(bin_str[:3], 2)
    packet_type = int(bin_str[3:6], 2)
    version_sum = packet_version
    print(packet_type, packet_version)

    if packet_type == 4:
        print('literal')
        bits = []

        idx = 6
        finished = False
        while not finished:
            bits.append(bin_str[idx + 1:idx + 5])
            finished = bin_str[idx] != '1'
            idx += 5
        print(bin_str[:len(bits) * 5 + 6])
        print(bits, len(bits) * 5 + 6)

        return packet_version, len(bits) * 5 + 6
    else:
        length_type = bin_str[6]

        if length_type == '0':
            sub_packet_length = int(bin_str[7: 22], 2)
            processed_length = 0
            idx = 22
            print('has sub-packets-length', sub_packet_length)
            while sub_packet_length > processed_length:
                sub_ver, pack_length = parse_packet(bin_str[idx:])
                version_sum += sub_ver
                processed_length += pack_length
                idx += pack_length
            return version_sum, idx

        else:
            num_sub_packets = int(bin_str[7: 18], 2)
            packets = 0

            print('has sub-packets', num_sub_packets)
            idx = 18
            while num_sub_packets > packets:
                sub_ver, pack_length = parse_packet(bin_str[idx:])
                idx += pack_length
                version_sum += sub_ver
                packets += 1

            return version_sum, idx


def handle_values(packet_type, values):
    if packet_type == 0:
        return sum(values)
    elif packet_type == 1:
        prod = 1
        for i in values:
            prod *= i
        return prod
    elif packet_type == 2:
        return min(values)
    elif packet_type == 3:
        return max(values)
    elif packet_type == 5:
        return 1 if values[0] > values[1] else 0
    elif packet_type == 6:
        return 1 if values[0] < values[1] else 0
    elif packet_type == 7:
        return 1 if values[0] == values[1] else 0


def parse_packet_p2(bin_str):
    print('looking at bin_str:', bin_str)
    packet_version = int(bin_str[:3], 2)
    packet_type = int(bin_str[3:6], 2)
    version_sum = packet_version
    print(packet_type, packet_version)

    if packet_type == 4:
        bits = []

        idx = 6
        finished = False
        while not finished:
            bits.append(bin_str[idx + 1:idx + 5])
            finished = bin_str[idx] != '1'
            idx += 5

        print('literal', int(''.join(bits), 2))
        return int(''.join(bits), 2), len(bits) * 5 + 6
    else:
        length_type = bin_str[6]

        if length_type == '0':
            sub_packet_length = int(bin_str[7: 22], 2)
            processed_length = 0
            idx = 22
            values = []
            print('has sub-packets-length', sub_packet_length)
            while sub_packet_length > processed_length:
                value, pack_length = parse_packet_p2(bin_str[idx:])
                values.append(value)
                processed_length += pack_length
                idx += pack_length
            return handle_values(packet_type, values), idx

        else:
            num_sub_packets = int(bin_str[7: 18], 2)
            packets = 0

            print('has sub-packets', num_sub_packets)
            idx = 18
            values = []
            while num_sub_packets > packets:
                value, pack_length = parse_packet_p2(bin_str[idx:])
                values.append(value)
                idx += pack_length
                packets += 1

            return handle_values(packet_type, values), idx


def day_sixteen(input_file):
    # lines = read_input.parse_lines(input_file)
    # base_grid = [[int(i) for i in row] for row in lines]

    # for line in lines:
    line = 'A0016C880162017C3686B18A3D4780'
    bin_str = ''
    for hex in line:
        bin_str += '{:04b}'.format(int(hex, 16))

    print(parse_packet(bin_str))


def day_sixteen_p2(input_file):
    line = '4057231006FF2D2E1AD8025275E4EB45A9ED518E5F1AB4363C60084953FB09E008725772E8ECAC312F0C18025400D34F732333DCC8FCEDF7CFE504802B4B00426E1A129B86846441840193007E3041483E4008541F8490D4C01A89B0DE17280472FE937C8E6ECD2F0D63B0379AC72FF8CBC9CC01F4CCBE49777098D4169DE4BF2869DE6DACC015F005C401989D0423F0002111723AC289DED3E64401004B084F074BBECE829803D3A0D3AD51BD001D586B2BEAFFE0F1CC80267F005E54D254C272950F00119264DA7E9A3E9FE6BB2C564F5376A49625534C01B0004222B41D8A80008446A8990880010A83518A12B01A48C0639A0178060059801C404F990128AE007801002803AB1801A0030A280184026AA8014C01C9B005CE0011AB00304800694BE2612E00A45C97CC3C7C4020A600433253F696A7E74B54DE46F395EC5E2009C9FF91689D6F3005AC0119AF4698E4E2713B2609C7E92F57D2CB1CE0600063925CFE736DE04625CC6A2B71050055793B4679F08CA725CDCA1F4792CCB566494D8F4C69808010494499E469C289BA7B9E2720152EC0130004320FC1D8420008647E8230726FDFED6E6A401564EBA6002FD3417350D7C28400C8C8600A5003EB22413BED673AB8EC95ED0CE5D480285C00372755E11CCFB164920070B40118DB1AE5901C0199DCD8D616CFA89009BF600880021304E0EC52100623A4648AB33EB51BCC017C0040E490A490A532F86016CA064E2B4939CEABC99F9009632FDE3AE00660200D4398CD120401F8C70DE2DB004A9296C662750663EC89C1006AF34B9A00BCFDBB4BBFCB5FBFF98980273B5BD37FCC4DF00354100762EC258C6000854158750A2072001F9338AC05A1E800535230DDE318597E61567D88C013A00C2A63D5843D80A958FBBBF5F46F2947F952D7003E5E1AC4A854400404A069802B25618E008667B7BAFEF24A9DD024F72DBAAFCB312002A9336C20CE84'
    bin_str = ''
    for hex in line:
        bin_str += '{:04b}'.format(int(hex, 16))

    print(parse_packet_p2(bin_str)[0])


def main():
    input_file = '16-example.in'
    input_file = '16.in'
    # day_sixteen(input_file)
    day_sixteen_p2(input_file)


main()
