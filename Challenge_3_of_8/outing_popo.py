# POPO File


class Outing:

    def __init__(self, outing_type, outing_cost_ind, outing_date, outing_attendance):
        self.outing_type = outing_type
        self.outing_cost_ind = outing_cost_ind
        self.outing_date = outing_date
        self.outing_attendance = outing_attendance
        self.event_cost = float(outing_cost_ind) * float(outing_attendance)

    def __repr__(self):
        return f"{self.outing_type} on {self.outing_date}: ${self.event_cost}"
