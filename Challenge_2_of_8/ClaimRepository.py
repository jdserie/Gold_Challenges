import claim_popo


claim_list = []


def list_all_claims(claimID, claimType, description, claimAmount, dateOfIncident, dateOfClaim, isValid):
    return claim_list


def justify_claims(isValid):
    return claim_list


def enter_claims_list(claimID, claimType, description, claimAmount, dateOfIncident, dateOfClaim, isValid):
    add_in = claim_popo.Claim(claimID, claimType, description, claimAmount, dateOfIncident, dateOfClaim, isValid)
    claim_list.append(add_in)
