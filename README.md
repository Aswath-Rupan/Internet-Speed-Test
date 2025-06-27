# Internet-Speed-Test
A minimal desktop widget built with Python and Tkinter to monitor internet speed (download, upload, ping) in real time, with CSV export support and automatic refresh.
________________

🛠 Features


* 🌐 Real-time monitoring of Download, Upload, and Ping

* 🔁 Automatically refreshes every 30 seconds

* 📁 Export last 60 readings to a timestamped CSV file

* 📌 Always stays on top of other windows

* 🧠 Smart detection of:

   * No internet

   * Connected to Wi-Fi but no actual internet access

   * No network connection

________________


📦 Requirements
      * Python 3.7+

      * speedtest-cli Python package

Install it using:
pip install speedtest-cli


________________


🚀 How to Run

1. Make sure the following two files are in the same directory:

	* main_widget.py – for the GUI

	* speed_test_logic.py – contains the test_speed() function

2. Run the main file:

	python main_widget.py


________________


📁 File Structure
internet-speed-widget/
├── speed_widget.py          # Main GUI logic
├── speed_test_logic.py     # Speed testing using speedtest module
├── README.txt               # Project documentation
└──LICENSE

________________


📤 Exporting to CSV

* Click the "Export Last 60 Readings" button to generate a .csv file.

The file is saved with a timestamped filename like:	speed_readings_20250627_113024.csv

* On Windows, it tries to auto-open the file after saving.

* If you open the file in Excel, you may need to manually widen the timestamp column to view the full date and time.

________________


⚠ Known Issues / Limitations

* 🕓 Slow first reading: The first speed test may take 1–2 minutes or more, depending on your network and system performance.

* 🔄 Temporary errors: You might see a connection error on startup, especially if your internet is temporarily unstable. This is usually self-resolving.

* 📉 UI delays: Since speed testing is done in the background, if the system or network is under load, updates may seem delayed.

* 📊 Excel formatting: When opening the exported CSV file in Excel, you may need to manually extend the timestamp column to see the full datetime value.

________________


✅ To-Do / Future Improvements

* Add a manual "Refresh Now" button

* Show timestamp of last successful test

* Add a graphical speed trend chart using matplotlib or tkinter.Canvas

* Optional tray icon support

* Auto start on boot (Windows)

________________


👨‍💻 Author
G Aswath Rupan
________________


📝 License
This project is licensed under the [MIT License](LICENSE)
