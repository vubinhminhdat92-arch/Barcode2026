import pandas as pd
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import os

# --- CẤU HÌNH ---
EXCEL_FILE = 'data.xlsx'  # Tên file Excel của bạn
OUTPUT_DIR = 'output_barcodes'
FONT_PATH = "arial.ttf" # Đường dẫn font (Window thường có sẵn)

def generate_label(row):
    # Lấy dữ liệu từ Excel
    ma_sp = str(row['MaSP'])
    ten_sp = str(row['TenSP'])
    gia = str(row['Gia'])
    
    # 1. Tạo mã vạch (Code128)
    code128 = barcode.get('code128', ma_sp, writer=ImageWriter())
    # Lưu tạm mã vạch
    barcode_img_path = f"temp_{ma_sp}"
    code128.save(barcode_img_path, options={"write_text": False, "module_height": 10.0})
    
    # 2. Mở ảnh mã vạch vừa tạo và trang trí thêm bằng Pillow
    img = Image.open(f"{barcode_img_path}.png")
    width, height = img.size
    
    # Tạo một khung ảnh mới lớn hơn để chứa thêm Text
    new_height = height + 150
    combined = Image.new('RGB', (width, new_height), (255, 255, 255))
    combined.paste(img, (0, 80)) # Đẩy mã vạch xuống giữa
    
    draw = ImageDraw.Draw(combined)
    
    # Chọn font (cần cài font vào máy hoặc để cùng thư mục)
    try:
        font_name = ImageFont.truetype(FONT_PATH, 30)
        font_price = ImageFont.truetype(FONT_PATH, 40)
    except:
        font_name = font_price = ImageFont.load_default()

    # Vẽ Tên Sản Phẩm
    draw.text((width/2, 30), ten_sp, fill="black", font=font_name, anchor="mm")
    
    # Vẽ Giá Tiền
    draw.text((width/2, new_height - 40), f"{gia} VND", fill="red", font=font_price, anchor="mm")
    
    # 3. Lưu ảnh cuối cùng
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    combined.save(f"{OUTPUT_DIR}/{ma_sp}.png")
    
    # Xóa file tạm
    os.remove(f"{barcode_img_path}.png")
    print(f"Đã tạo: {ma_sp} - {ten_sp}")

def main():
    try:
        df = pd.read_excel(EXCEL_FILE)
        # Lọc những dòng có dấu 'x' ở cột InMoi
        items_to_print = df[df['InMoi'].str.lower() == 'x']
        
        if items_to_print.empty:
            print("Không tìm thấy sản phẩm nào có dấu 'x'!")
            return

        for index, row in items_to_print.iterrows():
            generate_label(row)
            
        print(f"\nThành công! Toàn bộ ảnh nằm trong thư mục: {OUTPUT_DIR}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
