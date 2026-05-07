import streamlit as st
import cv2
from ultralytics import YOLO
import tensorflow as tf
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import interface # Import file giao diện riêng

# Cấu hình Streamlit
st.set_page_config(page_title="NHẬN DIỆN TRÁI CÂY", layout="wide")
st.markdown(interface.CSS_STYLE, unsafe_allow_html=True)
st.markdown(interface.HTML_HEADER, unsafe_allow_html=True)

# 1. Load các model (Dùng cache để không load lại nhiều lần)
@st.cache_resource
def load_models():
    yolo = YOLO('best1.pt')
    quality = tf.keras.models.load_model('quality_model_full.h5')
    return yolo, quality

yolo_model, quality_model = load_models()
quality_labels = ['Chat luong kem ❌', 'Chat luong tot ✅']

# Hàm xử lý chính (Giữ nguyên cấu trúc logic của bạn)
def process_frame(img):
    # Padding mở rộng để hiện đủ nhãn
    pad = 100 
    img_padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    img_display = img_padded.copy()
    
    results = yolo_model(img)
    analysis_results = []

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            yolo_label = yolo_model.names[cls_id] 
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            fruit_crop = img[y1:y2, x1:x2]
            
            if fruit_crop.size > 0:
                # Dự đoán chất lượng
                img_input = cv2.resize(fruit_crop, (160, 160))
                img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
                img_input = img_input.astype('float32') / 255.0
                img_input = np.expand_dims(img_input, axis=0)
                
                prediction = quality_model.predict(img_input, verbose=0)
                q_idx = np.argmax(prediction[0])
                conf_quality = np.max(prediction[0])
                
                # Hiển thị trên ảnh padded
                final_label = f"{yolo_label} - {quality_labels[q_idx]} ({conf_quality*100:.1f}%)"
                color = (0, 255, 0) if q_idx == 1 else (0, 0, 255)
                
                new_x1, new_y1 = x1 + pad, y1 + pad
                new_x2, new_y2 = x2 + pad, y2 + pad
                
                cv2.rectangle(img_display, (new_x1, new_y1), (new_x2, new_y2), color, 3)
                cv2.putText(img_display, final_label, (new_x1, new_y1 - 15), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                
                analysis_results.append({"label": yolo_label, "quality": quality_labels[q_idx], "conf": conf_quality})
                
    return img_display, analysis_results

# 2. Điều khiển Sidebar
st.sidebar.title("Chế độ đầu vào")
mode = st.sidebar.radio("Chọn phương thức:", [" Upload Ảnh", " Live Camera"])

if mode == " Upload Ảnh":
    uploaded_file = st.file_uploader("Chọn ảnh trái cây...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        with st.spinner('Đang phân tích...'):
            res_img, data = process_frame(img)
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.image(cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB), use_column_width=True)
            with col2:
                st.markdown("Kết quả chi tiết")
                for item in data:
                    st.markdown(interface.get_result_card(item['label'], item['quality'], item['conf']), unsafe_allow_html=True)

else:
    st.info("Hãy nhấn Start để bắt đầu quét Camera")
    class VideoProcessor(VideoTransformerBase):
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            res_img, _ = process_frame(img)
            return res_img

    webrtc_streamer(key="fruit-detection", video_transformer_factory=VideoProcessor)