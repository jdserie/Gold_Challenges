# POPO File


class Claim:

    def __init__(self, claimID, claimType, description, claimAmount, dateOfIncident, dateOfClaim, isValid):
        self.claimID = claimID
        self.claimType = claimType
        self.description = description
        self.claimAmount = claimAmount
        self.dateOfIncident = dateOfIncident
        self.dateOfClaim = dateOfClaim
        self.isValid = isValid

    def __repr__(self):
        return f'\nClaim ID: {self.claimID}, Claim Type: {self.claimType}, Claim Description: {self.description}, Claim Amount: ${self.claimAmount}, Date of Incident: {self.dateOfIncident}, Date of Claim: {self.dateOfClaim}, Claim Validity: {self.isValid}'
