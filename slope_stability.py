def calculate_slope_stability(slope_angle, cohesion, unit_weight, height, phi, water_table_depth):
    # Factor of Safety (FS) using simplified method
    num = cohesion + (unit_weight * height * math.cos(math.radians(slope_angle)) * math.tan(math.radians(phi)))
    den = unit_weight * height * math.sin(math.radians(slope_angle))
    
    FS = num / den
    
    # Reduce FS if the water table is present
    if water_table_depth < height:
        FS *= 0.8  # Adjust factor of safety to account for the water table
    
    return round(FS, 2)
