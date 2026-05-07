# interface.py

# 1. Định nghĩa CSS
CSS_STYLE = """
<style>
    .result-card {
        background: white; 
        padding: 15px; 
        border-radius: 10px;
        border-left: 5px solid #ffc107; 
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        color: #333;
    }
</style>
"""

# 2. Định nghĩa Header
HTML_HEADER = """
<div class="main-header">
    <h1 style='color: #1b5e20;'>🍎 HỆ THỐNG AI KIỂM ĐỊNH TRÁI CÂY</h1>
    <p style='color: #666;'>Nhận diện chủng loại & Đánh giá chất lượng thực tế</p>
</div>
"""

# 3. Hàm tạo thẻ kết quả
def get_result_card(label, quality, conf):
    # Dùng f-string để truyền dữ liệu vào HTML
    return f'''
    <div class="result-card">
        <b style="color: #1b5e20;">Loại quả:</b> {label}<br>
        <b style="color: #1b5e20;">Đánh giá:</b> {quality}<br>
        <b style="color: #1b5e20;">Độ chính xác:</b> {conf*100:.1f}%
    </div>
    '''