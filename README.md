# detect_fruit
Chào bạn, một file README.md chuyên nghiệp sẽ giúp người khác (hoặc chính bạn trong tương lai) hiểu cách cài đặt và vận hành hệ thống một cách nhanh chóng.

Dưới đây là nội dung file README được thiết kế riêng cho dự án của bạn:

🍎 Hệ thống AI Nhận diện & Đánh giá Chất lượng Trái cây
Hệ thống ứng dụng trí tuệ nhân tạo (AI) để tự động nhận diện loại trái cây, trạng thái chín và đánh giá chất lượng (Tốt/Kém) thông qua hình ảnh hoặc Camera trực tiếp. Dự án sử dụng kết hợp YOLOv8 (Nhận diện vật thể) và MobileNetV2 (Phân loại chất lượng).

🌟 Tính năng nổi bật
Nhận diện đa năng: Hỗ trợ Chuối, Xoài, Lựu với các trạng thái Xanh/Chín.

Đánh giá chất lượng: Phân loại trái cây thành "Chất lượng tốt" hoặc "Chất lượng kém" dựa trên đặc điểm bề mặt.

Giao diện Web: Tích hợp Streamlit cho phép tải ảnh lên hoặc quay Camera realtime.

Xử lý thông minh: Tự động mở rộng khung hình (Padding) để nhãn không bị che khuất khi trái cây nằm sát mép ảnh.

🛠 Công nghệ sử dụng
Ngôn ngữ: Python 3.9+

AI Frameworks: * Ultralytics (YOLOv8)

TensorFlow/Keras (MobileNetV2)

Web Framework: Streamlit

Thư viện hỗ trợ: OpenCV, NumPy, Streamlit-WebRTC

📂 Cấu trúc thư mục
Plaintext
Fruit_detection/
├── app.py                 # File xử lý logic AI và Streamlit chính

├── interface.py           # Chứa giao diện HTML/CSS riêng biệt

├── best1.pt               # Model YOLOv8 nhận diện loại quả

├── quality_model_full.h5   # Model Keras đánh giá chất lượng

└── requirements.txt       # Danh sách các thư viện cần cài đặt
🚀 Hướng dẫn cài đặt
1. Cài đặt môi trường
Đảm bảo bạn đã cài đặt Python, sau đó mở Terminal và chạy lệnh:

Bash
pip install streamlit ultralytics tensorflow opencv-python numpy streamlit-webrtc
2. Chuẩn bị Model
Đặt các file model best1.pt và quality_model_full.h5 vào cùng thư mục với file app.py.

3. Khởi chạy ứng dụng
Bash
streamlit run app.py
🎮 Hướng dẫn sử dụng
Chế độ Upload: Chọn "📤 Tải ảnh từ máy" ở thanh sidebar, kéo thả ảnh trái cây vào. Hệ thống sẽ hiển thị kết quả phân tích chi tiết ở cột bên phải.

Chế độ Live: Chọn "🎥 Live Camera", nhấn nút Start để bắt đầu quét trái cây trực tiếp từ Webcam.

📊 Danh sách nhãn hỗ trợ
YOLO (Trạng thái): Raw Banana, Ripe Banana, Raw Mango, Ripe Mango, Early/Mid/Ripe Pomegranate.

Chất lượng: Tốt (✅), Kém (❌).
