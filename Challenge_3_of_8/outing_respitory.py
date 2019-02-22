# I am aware I spelled Repository wrong.
# I noticed last second and decided to leave it be, because the code is set to typo, and works

import outing_popo

outing_list = []


def list_all_events():
    return outing_list


def add_event(outing_type, outing_cost_ind, outing_date, outing_attendance):
    tmp = outing_popo.Outing(outing_type, outing_cost_ind, outing_date, outing_attendance)
    outing_list.append(tmp)


def calc_by_type(outing_type):                        # INPUT = Parameter
    total_a = 0
    for y in outing_list:
        if y.outing_type == outing_type:
            total_a += y.event_cost
    return total_a                                    # OUTPUT = Return


def calc_overall():
    total_b = 0
    for x in outing_list:
        total_b += x.event_cost
    return total_b
