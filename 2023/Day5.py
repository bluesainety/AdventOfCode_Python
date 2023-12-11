from helper import file_handler as fh

class RangeMap:
    start = 0
    end = 0
    mod = 0
    size = 0

    range = range(0, 0)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_mod(self):
        return self.mod

    def get_destination_start(self):
        return self.start + self.mod

    def contains(self, value):
        return self.start <= value < self.end

    def destination_contains(self, value):
        return (self.start + self.mod) <= value < (self.end + self.mod)

    def modify(self, value):
        value += self.mod
        return value

    def __init__(self, start, end, mod):
        self.start = start
        self.end = end
        self.mod = mod
        self.range = range(start, end)
        self.size = end - start


def maps_from_lines(lines):
    maps = []

    for line in lines:
        values = line.split(' ')
        maps.append(RangeMap(int(values[1]), int(values[1]) + int(values[2]), int(values[0]) - int(values[1])))

    maps.sort(key=RangeMap.get_start)

    if maps[0].get_start() != 0:
        maps.insert(0, RangeMap(0, maps[0].get_start(), 0))

    toAdd = []

    for i in range(len(maps)-1):
        if maps[i].get_end() != maps[i+1].get_start():
            toAdd.append(RangeMap(maps[i].get_end(), maps[i+1].get_start(), 0))

    maps += toAdd
    maps.sort(key=RangeMap.get_start)

    return maps


def get_lines_from_to_str(lines, from_str, to_str):
    for i in range(len(lines)):
        if lines[i] == from_str:
            temp_lines = []
            counter = 1
            while (i + counter) != len(lines) and lines[i + counter] != to_str:
                temp_lines.append(lines[i + counter])
                counter += 1
            return temp_lines


def process_input():
    lines = fh.readLinesFromFile("Inputs/Day5.txt")

    seeds = lines[0].split(' ')[1:]

    seed_to_soil_maps = maps_from_lines(get_lines_from_to_str(lines, "seed-to-soil map:", ""))
    soil_to_fertilizer_maps = maps_from_lines(get_lines_from_to_str(lines, "soil-to-fertilizer map:", ""))
    fertilizer_to_water_maps = maps_from_lines(get_lines_from_to_str(lines, "fertilizer-to-water map:", ""))
    water_to_light_maps = maps_from_lines(get_lines_from_to_str(lines, "water-to-light map:", ""))
    light_to_temperature_maps = maps_from_lines(get_lines_from_to_str(lines, "light-to-temperature map:", ""))
    temperature_to_humidity_maps = maps_from_lines(get_lines_from_to_str(lines, "temperature-to-humidity map:", ""))
    humidity_to_location_maps = maps_from_lines(get_lines_from_to_str(lines, "humidity-to-location map:", ""))

    maps_in_order = [seed_to_soil_maps, soil_to_fertilizer_maps, fertilizer_to_water_maps, water_to_light_maps, light_to_temperature_maps, temperature_to_humidity_maps, humidity_to_location_maps]
    return seeds, maps_in_order


def findMapForValue(value, map_list: list[RangeMap]) -> RangeMap:
    for map in map_list:
        if map.contains(value):
            return map

    return RangeMap(0,0,0)


def value_to_x(value, start, end, maps_in_order):

    while start < end:
        range_map = findMapForValue(value, maps_in_order[start])
        value = range_map.modify(value)
        start += 1

    return value


def part1():
    seeds, maps_in_order = process_input()
    seed_results = []

    for seed in seeds:
        seed_results.append(value_to_x(int(seed), 0, 7, maps_in_order))

    return seed_results


def find_maps_for_range(range_m: RangeMap, maps_in_order: list[RangeMap]):
    maps = []

    for i in range(len(maps_in_order)):
        if maps_in_order[i].contains(range_m.get_start()):
            maps.append(maps_in_order[i])
            if i == (len(maps_in_order)-1) or maps_in_order[i].contains(range_m.get_end()):
                break;

            while i < (len(maps_in_order)-1) and not maps_in_order[i].contains(range_m.get_end()):
                maps.append(maps_in_order[i])
                i += 1

            maps.append(maps_in_order[i])
            break;
        i += 1

    if len(maps) == 0:
        maps.append(RangeMap(range_m.get_start(), range_m.get_end(), 0))

    return maps


def map_bits(seed_map: RangeMap, map_list: list[list[RangeMap]], i):

    next_maps = find_maps_for_range(seed_map, map_list[i])

    temp_maps = []
    modified_next_maps = []

    for map_ in next_maps:
        map_start = seed_map.get_start() if seed_map.get_start() > map_.get_start() \
            else map_.get_start()
        map_end = seed_map.get_end() if seed_map.get_end() < map_.get_end() \
            else map_.get_end()

        temp_maps.append(RangeMap(map_start + map_.get_mod(), map_end + map_.get_mod(),0))

    if i > 5:
        return temp_maps

    for temp_map in temp_maps:
        modified_next_maps += map_bits(temp_map, map_list, i + 1)

    return modified_next_maps


def part2():
    seeds, maps_in_order = process_input()
    seed_maps = []

    i = 0
    while i in range(len(seeds)):
        seed_maps.append(RangeMap(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]), 0))
        i += 2

    minimums = []

    for seed_map in seed_maps:
        final_maps = map_bits(seed_map, maps_in_order, 0)
        final_maps.sort(key=RangeMap.get_start)
        minimums.append(final_maps[0].get_start())

    return minimums


def main():
    minimums = part2()
    print(minimums)
    print(min(minimums))


if __name__ == "__main__":
    main()