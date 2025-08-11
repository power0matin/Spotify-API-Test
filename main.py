import requests
import time
import datetime
import os

LOG_DIR = "Log"
GITHUB_LINK = "https://github.com/power0matin/SpotyMate-VPS-API-Test"

def ensure_log_dir():
    """Ensure the log directory exists."""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def get_log_file_path():
    """Generate a timestamped log file path."""
    now = datetime.datetime.now()
    filename = now.strftime("spotify_api_test_%Y-%m-%d_%H-%M-%S.log")
    return os.path.join(LOG_DIR, filename)

def log(message: str, log_file):
    """Write message to log file with timestamp and print it."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    log_file.write(full_message + "\n")
    log_file.flush()

def test_spotify_api(log_file):
    """Perform a test GET request to Spotify API and log the results."""
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SpotyMateBotTest/1.0)",
    }
    try:
        log(f"Designed by power0matin | GitHub: {GITHUB_LINK}", log_file)
        log(f"Sending GET request to {url}", log_file)
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        duration = time.time() - start_time

        log(f"Status Code: {response.status_code}", log_file)
        log(f"Response Time: {duration:.3f} seconds", log_file)
        log("Response Headers:", log_file)
        for k, v in response.headers.items():
            log(f"  {k}: {v}", log_file)

        if response.status_code == 200:
            log("✅ Success: Spotify API accessible!", log_file)
        elif response.status_code == 403:
            log("⛔ Forbidden: Spotify API access blocked on this VPS.", log_file)
        else:
            log("⚠️ Unexpected response:", log_file)
            log(response.text, log_file)

    except requests.exceptions.RequestException as e:
        log(f"Request failed: {e}", log_file)

if __name__ == "__main__":
    ensure_log_dir()
    log_path = get_log_file_path()
    with open(log_path, "a") as log_file:
        log("="*40, log_file)
        test_spotify_api(log_file)
        print(f"\n📝 Log has been saved to: {log_path}\n")