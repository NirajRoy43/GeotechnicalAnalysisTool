def calculate_total_settlement(immediate_settlement, consolidation_settlement):
    # Total settlement = Immediate settlement + Consolidation settlement
    total_settlement = immediate_settlement + consolidation_settlement
    return round(total_settlement, 2)
