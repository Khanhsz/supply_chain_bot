def classify_problem(text):
    text = text.lower()
    if "break-even" in text or "hòa vốn" in text:
        return "break_even"
    elif "eoq" in text or "economic order quantity" in text or "số lượng đặt hàng" in text:
        return "eoq"
    elif "safety inventory" in text or "tồn kho an toàn" in text or "continuous review" in text:
        return "safety_inventory"
    elif "expected value" in text or "giá trị kỳ vọng" in text:
        return "supplier_selection"
    elif "batch picking" in text or "lô hàng" in text:
        return "batch_picking"
    else:
        return "general_mcq"