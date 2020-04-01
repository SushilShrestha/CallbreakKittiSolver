POINTS_TABLE = {
    'POWER': {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11,
        13: 12,
        1: 13,
    },
    'JUDH': {
        2: 14,
        3: 15,
        4: 16,
        5: 17,
        6: 18,
        7: 19,
        8: 20,
        9: 21,
        10: 22,
        11: 23,
        12: 24,
        13: 25,
        1: 26,
    },
    'COLOR': {
        5: 28,
        6: 29,
        7: 30,
        8: 31,
        9: 32,
        10: 33,
        11: 34,
        12: 35,
        13: 36,
        1: 37,
    },
    'RUNS': {
        2: 40,
        3: 41,
        4: 42,
        5: 43,
        6: 44,
        7: 45,
        8: 46,
        9: 47,
        10: 48,
        11: 49,
        12: 50,
        1: 51,
    },
    'DOUBLE_RUNS': {
        2: 53,
        3: 54,
        4: 55,
        5: 56,
        6: 57,
        7: 58,
        8: 59,
        9: 60,
        10: 61,
        11: 62,
        12: 63,
        1: 64,
    },
    'TRAIL': {
        2: 66,
        3: 67,
        4: 68,
        5: 69,
        6: 70,
        7: 71,
        8: 72,
        9: 73,
        10: 74,
        11: 75,
        12: 76,
        13: 77,
        1: 78,
    },

}

def memoize(function):
    memo = {}
    def wrapper(*args):
        cache_key = str(args[0][0]) + str(args[0][1]) + str(args[0][2])
        if cache_key in memo:
            return memo[cache_key]

        receive_value = function(*args)
        memo[cache_key] = receive_value
        # print args
        return receive_value
    return wrapper


@memoize
def calculate_point(sorted_three_card_seq):
    # from Cards import print_cards
    # print_cards(sorted_three_card_seq)
    try:
        if is_trail(sorted_three_card_seq):
            # print 'trail'
            return trail_points(sorted_three_card_seq)
        elif is_a_double_run(sorted_three_card_seq):
            # print 'double run'
            return double_run_point(sorted_three_card_seq)
        elif is_a_run(sorted_three_card_seq):
            # print 'run'
            return run_point(sorted_three_card_seq)
        elif is_of_same_color(sorted_three_card_seq):
            # print 'france'
            return color_point(sorted_three_card_seq)
        elif is_a_judh(sorted_three_card_seq):
            # print 'double'
            return judh_point(sorted_three_card_seq)
        # print 'power'
        return power_point(sorted_three_card_seq)
    except Exception, exc:
        from cards import print_cards
        print_cards(sorted_three_card_seq)
        raise exc


def is_trail(triplet):
    return (
        triplet[0].has_same_number(triplet[1]) and
        triplet[0].has_same_number(triplet[2])
    )


def is_a_double_run(triplet):
    return is_a_run(triplet) and is_of_same_color(triplet)


def is_a_run(sorted_triplet):
    if sorted_triplet[0].number == 1 and sorted_triplet[1].number == 12 \
            and sorted_triplet[2].number == 13:
        return True
    return sorted_triplet[0].number + 2 == sorted_triplet[1].number + 1 == \
           sorted_triplet[2].number


def is_of_same_color(triplet):
    return triplet[0].suit == triplet[1].suit == triplet[2].suit


def is_a_judh(triplet):
    # if is_trail(triplet):
    #     return False
    return (
        triplet[0].has_same_number(triplet[1]) or
        triplet[0].has_same_number(triplet[2]) or
        triplet[1].has_same_number(triplet[2])
    )


def trail_points(triplet):
    point = POINTS_TABLE['TRAIL'][triplet[0].number]
    return point


def double_run_point(triplet):
    min_card = min(triplet, key=lambda x: x.number)
    if min_card == 1:
        point = POINTS_TABLE['DOUBLE_RUNS'][12]
        return point

    point = POINTS_TABLE['DOUBLE_RUNS'][min_card.number]
    return point


def run_point(triplet):
    min_card = min(triplet, key=lambda x: x.number)
    if min_card == 1:
        point = POINTS_TABLE['RUNS'][12]
        return point

    point = POINTS_TABLE['RUNS'][min_card.number]
    return point


def color_point(triplet):
    min_card = triplet[0]
    if min_card.number == 1:
        points = POINTS_TABLE['COLOR'][1] + get_extra_power_point(*triplet[1:])
        return points

    max_card = triplet[2]
    points = POINTS_TABLE['COLOR'][max_card.number] + get_extra_power_point(*triplet[:2])
    return points


def judh_point(triplet):
    judh_card = None
    non_judh_card = None

    if triplet[0].has_same_number(triplet[1]):
        judh_card = triplet[0]
        non_judh_card = triplet[2]
    elif triplet[0].has_same_number(triplet[2]):
        judh_card = triplet[0]
        non_judh_card = triplet[1]
    else:
        judh_card = triplet[1]
        non_judh_card = triplet[0]

    point = POINTS_TABLE['JUDH'][judh_card.number] + get_extra_power_point(non_judh_card)
    return point


def power_point(triplet):
    min_card = triplet[0]
    if min_card.number == 1:
        return POINTS_TABLE['POWER'][1] + get_extra_power_point(*triplet[1:])

    return POINTS_TABLE['POWER'][triplet[2].number] + get_extra_power_point(*triplet[:2])


def get_extra_power_point(*args):
    divider = 13 * len(args)
    points = [POINTS_TABLE['POWER'][x.number] for x in args]
    total_point = reduce(lambda x, y: x + y, points, 0)
    return float(total_point) / divider


if __name__ == '__main__':
    from cards import Card

    c_aaa = [Card(1, 'hearts'), Card(1, 'diamonds'), Card(1, 'clubs')]
    c_kkk = [Card(13, 'hearts'), Card(13, 'diamonds'), Card(13, 'clubs')]
    c_222 = [Card(2, 'hearts'), Card(2, 'diamonds'), Card(2, 'clubs')]
    c_akq_dr = [Card(1, 'hearts'), Card(13, 'hearts'), Card(12, 'hearts')]
    c_910j_dr = [Card(9, 'hearts'), Card(11, 'hearts'), Card(10, 'hearts')]
    c_234_dr = [Card(2, 'hearts'), Card(3, 'hearts'), Card(4, 'hearts')]
    c_akq = [Card(1, 'hearts'), Card(13, 'clubs'), Card(12, 'spades')]
    c_8910 = [Card(9, 'clubs'), Card(8, 'hearts'), Card(10, 'hearts')]
    c_234 = [Card(2, 'spades'), Card(3, 'clubs'), Card(4, 'hearts')]
    c_akj_clr = [Card(1, 'hearts'), Card(13, 'hearts'), Card(11, 'hearts')]
    c_7j9_clr = [Card(7, 'hearts'), Card(11, 'hearts'), Card(9, 'hearts')]
    c_235_clr = [Card(2, 'hearts'), Card(3, 'hearts'), Card(5, 'hearts')]
    c_aak = [Card(1, 'hearts'), Card(1, 'clubs'), Card(13, 'clubs')]
    c_k55 = [Card(13, 'hearts'), Card(5, 'diamonds'), Card(5, 'clubs')]
    c_223 = [Card(2, 'hearts'), Card(3, 'diamonds'), Card(2, 'clubs')]
    c_akj = [Card(1, 'hearts'), Card(13, 'diamonds'), Card(11, 'clubs')]
    c_j68 = [Card(11, 'hearts'), Card(6, 'diamonds'), Card(8, 'clubs')]
    c_235 = [Card(2, 'hearts'), Card(3, 'diamonds'), Card(5, 'clubs')]

    print calculate_point(sorted(c_aaa, key=lambda x: x.number))
    print calculate_point(sorted(c_kkk, key=lambda x: x.number))
    print calculate_point(sorted(c_222, key=lambda x: x.number))
    print calculate_point(sorted(c_akq_dr, key=lambda x: x.number))
    print calculate_point(sorted(c_910j_dr, key=lambda x: x.number))
    print calculate_point(sorted(c_234_dr, key=lambda x: x.number))
    print calculate_point(sorted(c_akq, key=lambda x: x.number))
    print calculate_point(sorted(c_8910, key=lambda x: x.number))
    print calculate_point(sorted(c_234, key=lambda x: x.number))
    print calculate_point(sorted(c_akj_clr, key=lambda x: x.number))
    print calculate_point(sorted(c_7j9_clr, key=lambda x: x.number))
    print calculate_point(sorted(c_235_clr, key=lambda x: x.number))
    print calculate_point(sorted(c_aak, key=lambda x: x.number))
    print calculate_point(sorted(c_k55, key=lambda x: x.number))
    print calculate_point(sorted(c_223, key=lambda x: x.number))
    print calculate_point(sorted(c_akj, key=lambda x: x.number))
    print calculate_point(sorted(c_j68, key=lambda x: x.number))
    print calculate_point(sorted(c_235, key=lambda x: x.number))
