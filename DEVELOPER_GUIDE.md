# Hướng dẫn Phát triển & Nâng cấp (Developer Guide)

Ứng dụng: **Barcode Studio Ultimate 2026**
Phiên bản: 1.0.0 (Web Edition)

## 1. Công nghệ sử dụng (Tech Stack)
- **Framework:** React 19 + Vite
- **Styling:** Tailwind CSS (Theme: High Density)
- **Barcode Engine:** `JsBarcode` (Canvas-based)
- **Excel Processing:** `xlsx` (SheetJS)
- **Export System:** `jszip` & `file-saver`

## 2. Cấu trúc mã nguồn
- `/src/App.tsx`: Chứa toàn bộ giao diện điều khiển, quản lý trạng thái (State) và luồng xử lý dữ liệu.
- `/src/types.ts`: Định nghĩa các tham số của nhãn (Price, Name, Styles, X/Y Offset...). Đây là nơi bạn thêm các thuộc tính mới cho tem.
- `/src/lib/barcodeGenerator.ts`: Chứa logic vẽ tem nhãn lên Canvas. Mọi thay đổi về cách trình bày tem (vị trí, font, gạch chân...) đều nằm ở đây.
- `/src/index.css`: Chứa các biến màu sắc (CSS Variables) của giao diện "High Density".

## 3. Logic quan trọng
- **Tùy chỉnh riêng lẻ:** Sử dụng thuộc tính `customParams` trong mảng `bulkData`. Khi `selectedIndex !== -1`, hệ thống sẽ ưu tiên lấy thông số từ `customParams` thay vì `templateParams`.
- **Xuất hàng loạt:** Hệ thống lọc các dòng có giá trị `"x"` trong cột `InMoi` (không phân biệt hoa/thường) trước khi nén vào ZIP.
- **Tự động xuống hàng:** Sử dụng logic chia nhỏ chuỗi theo từ (words) và đo độ rộng bằng `ctx.measureText` để quyết định khi nào cần `lines.push()`.

## 4. Cách chạy trên máy tính cá nhân
1. Cài đặt **Node.js** (phiên bản 18 trở lên).
2. Tải mã nguồn về và giải nén.
3. Mở terminal tại thư mục dự án và chạy: `npm install`
4. Chạy ứng dụng ở chế độ phát triển: `npm run dev`
5. Đóng gói để đưa lên web: `npm run build`

## 5. Hướng nâng cấp gợi ý
- Thêm tính năng lưu các bộ thông số (Presets) vào trình duyệt (LocalStorage).
- Hỗ trợ thêm nhiều định dạng mã vạch khác (QR Code, EAN-8...).
- Thêm tính năng chọn ảnh nền cho tem nhãn.

---
*Tài liệu này được tạo tự động để hỗ trợ bảo trì và nâng cấp dự án.*
