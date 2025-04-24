import os
import shutil
import schedule
import time
from datetime import datetime
from Tudongguimail import send_email

SOURCE_FOLDER = "./Data/databases/My.sqlite3"
BACKUP_FOLDER = "./Data/backup"
sender_email = "123@gmail.com"
app_password = "123"
receiver_email = "321@gmail.com"
subject = "Thông báo tự động"
body = "Đây là email tự động được gửi từ Python. Không cần trả lời email này."

def backup_database():
    try:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        files_copied = []

        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)

        for filename in os.listdir(SOURCE_FOLDER):
            if filename.endswith(".sql") or filename.endswith(".sqlite3"):
                src_path = os.path.join(SOURCE_FOLDER, filename)
                dest_path = os.path.join(BACKUP_FOLDER, f"{now}_{filename}")
                shutil.copy2(src_path, dest_path)
                files_copied.append(dest_path)

        if files_copied:
            send_email(
                subject="Backup thành công",
                message=f"Đã backup các file: \n" + "\n".join(files_copied)
            )
        else:
            send_email(
                subject="Backup không có file",
                message="Không tìm thấy file .sql hoặc .sqlite3 để backup."
            )

    except Exception as e:
        send_email(
            subject="Backup thất bại",
            message=f"Lỗi: {str(e)}"
        )


schedule.every().day.at("00:00").do(backup_database)

print("Đang chạy backup scheduler")
while True:
    schedule.run_pending()
    time.sleep(60)