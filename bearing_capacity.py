import math

def calculate_bearing_capacity(cohesion, unit_weight, depth, width, surcharge, phi):
    # Terzaghi's bearing capacity factors
    Nq = math.exp(math.pi * math.tan(math.radians(phi))) * (1 + math.sin(math.radians(phi)))**2 / (1 - math.sin(math.radians(phi)))**2
    Nc = (Nq - 1) / math.tan(math.radians(phi))
    Ngamma = 2 * (Nq + 1) * math.tan(math.radians(phi))
    
    # Calculation of ultimate bearing capacity
    qult = (cohesion * Nc) + (surcharge * Nq) + (0.5 * unit_weight * width * Ngamma)

    # Applying factor of safety
    factor_of_safety = 3
    qsafe = qult / factor_of_safety

    return round(qsafe, 2)
