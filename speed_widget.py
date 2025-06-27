import tkinter as tk
from tkinter import ttk
import threading
import datetime
import csv
import os
import socket
from speed_test_logic import test_speed  # From separate file

REFRESH_INTERVAL = 60  # seconds

class SpeedTestWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Widget")
        self.root.geometry("270x190")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        self.root.attributes("-topmost", True)

        style = ttk.Style()
        style.configure("TLabel", foreground="white", background="#1e1e1e", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 9), padding=3)

        self.label_download = ttk.Label(root, text="Download: -- Mbps")
        self.label_download.pack(pady=4)

        self.label_upload = ttk.Label(root, text="Upload: -- Mbps")
        self.label_upload.pack(pady=4)

        self.label_ping = ttk.Label(root, text="Ping: -- ms")
        self.label_ping.pack(pady=4)

        self.label_error = ttk.Label(root, text="", foreground="orange", background="#1e1e1e", font=("Segoe UI", 9))
        self.label_error.pack(pady=4)

        self.export_button = ttk.Button(root, text="Export Last 60 Readings", command=self.save_readings_to_csv)
        self.export_button.pack(pady=4)

        self.readings = []  # To store the last 60 results

        self.update_speed()

    def is_connected(self, host="8.8.8.8", port=53, timeout=3):
        """Check if there is an active internet connection"""
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False

    def update_speed(self):
        def run():
            timestamp = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            try:
                # Check if connected to any network
                hostname = socket.gethostbyname(socket.gethostname())
                if hostname.startswith("127.") or hostname == "":
                    raise Exception("Not connected to any network")

                # Check for actual internet access
                if not self.is_connected():
                    self.label_error.config(text="❌ Connected to Wi-Fi, but no internet")
                else:
                    # Run the speed test
                    download, upload, ping = test_speed()
                    self.label_download.config(text=f"Download: {download} Mbps")
                    self.label_upload.config(text=f"Upload: {upload} Mbps")
                    self.label_ping.config(text=f"Ping: {ping} ms")
                    self.label_error.config(text="")  # Clear error

                    self.readings.append({
                        "timestamp": timestamp,
                        "download": download,
                        "upload": upload,
                        "ping": ping
                        })

                    # Keep only last 60 readings
                    if len(self.readings) > 60:
                        self.readings.pop(0)

            except Exception as e:
                self.label_error.config(text="❌ No network connection or test error")

            # ✅ Always schedule next update
            self.root.after(REFRESH_INTERVAL * 1000, self.update_speed)

        threading.Thread(target=run).start()

    def save_readings_to_csv(self):
        if not self.readings:
            self.label_error.config(text="⚠️ No readings to export yet.")
            return

        filename = f"speed_readings_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
                writer = csv.DictWriter(file, fieldnames=["timestamp", "download", "upload", "ping"])
                writer.writeheader()
                writer.writerows(self.readings)

            self.label_error.config(text=f"✅ Saved: {filename}")

            # Auto-open in Excel (Windows only)
            try:
                os.startfile(filename)
            except:
                pass

        except Exception as e:
            self.label_error.config(text=f"❌ Error saving CSV")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestWidget(root)
    root.mainloop()
