def calculate_consolidation_settlement(compression_index, initial_void_ratio, layer_thickness, applied_stress, preconsolidation_stress):
    # Calculate settlement using the classical consolidation formula
    if applied_stress > preconsolidation_stress:
        stress_increase = applied_stress - preconsolidation_stress
        settlement = (compression_index / (1 + initial_void_ratio)) * layer_thickness * math.log10((preconsolidation_stress + stress_increase) / preconsolidation_stress)
    else:
        settlement = 0  # No consolidation if stress is less than preconsolidation
    
    return round(settlement, 2)
