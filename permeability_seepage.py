def calculate_seepage_rate(permeability, area, hydraulic_gradient):
    # Seepage rate through the soil (Darcy's Law)
    seepage_rate = permeability * area * hydraulic_gradient
    return round(seepage_rate, 4)
