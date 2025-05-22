import re
import math

def solve_eoq(text):
    try:
        D = float(re.search(r"(?i)\b(?:demand|nhu cầu)\D*(\d+[\d\.]*)", text).group(1))
        S = float(re.search(r"(?i)\b(?:ordering cost|chi phí đặt hàng)\D*(\d+[\d\.]*)", text).group(1))
        H = float(re.search(r"(?i)\b(?:holding cost|chi phí lưu kho)\D*(\d+[\d\.]*)", text).group(1))
    except:
        return "❗ Không thể trích xuất dữ kiện. Please format your input more clearly."

    eoq = math.sqrt((2 * D * S) / H)
    solution = f'''
    **Công thức / Formula:**
    EOQ = √((2 × D × S) / H)

    **Thay số / Substitute values:**
    EOQ = √((2 × {D} × {S}) / {H}) = {eoq:.2f}

    ✅ **Kết luận / Conclusion:** Số lượng đặt hàng tối ưu là {eoq:.2f} đơn vị.
    '''
    return solution