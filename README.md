# 🍄 Super One-Way Followers Bros 🍄

## 🌟 [MARIO-themed WEBSITE](https://janbacer.github.io/OneWayFollowers_Instagram/) 🌟

### 🕹️ Web Edition Highlights:
- **Live Physics:** Mario and Koopas roam your results!
- **Interactive:** Stomp, kick shells, and collect coins!
- **Zero-Install:** Analyze your data directly in your browser.

---

# Instagram One-Way Followers 

Have you ever wanted to know who are you flloiwng but doesnt follow back?
With this tool now you can easily unfollow, disloyal followers

This tool helps you analyze your Instagram data export to find out:
- Who you follow that doesn't follow you back
- Your pending follow requests

Working as of 12-03-2026, Instagram version 420.0.0.55.74.

## Features

- Simple graphical interface (Tkinter)
- Supports both HTML and JSON Instagram data exports
- Displays results in easy-to-read columns

## Dependencies

- Python 3.9+
- beautifulsoup4

Install dependency:

```sh
python -m pip install --user beautifulsoup4
```

Notes:
- `tkinter`, `json`, `zipfile`, `tempfile`, `math`, and `os` are part of Python standard library.

## How to Use

1. **Download your Instagram data**  
   Go to the [Instagram Accounts Center](https://accountscenter.instagram.com/info_and_permissions/dyi/) and request your information.  
   Click **Create export** > **Export to device**.  
   For **Date Range**, select **From the Beginning**.  
   Click **Start Export**.  
   Wait to receive an email with the download link (this may take up to a day).

2. **Run the App**  
   Double-click `main.exe`  
   *or*  
   Run from terminal:
   ```sh
   python main.py
   ```

3. **Select your Instagram ZIP file**  
   Use the file dialog to select your downloaded ZIP.

4. **View Results**  
   The app will show:
   - People you follow who don’t follow you back
   - Pending follow requests

## Notes

- No Instagram login required.
- Your data stays on your computer.
