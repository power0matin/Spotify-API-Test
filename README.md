<h1 align="center">🎧 Spotify-API-Test 🚀</h1>

<!-- repo-badges:start -->

<p align="center">
  <a href="https://hits.sh/github.com/power0matin/Spotify-API-Test/"><img src="https://hits.sh/github.com/power0matin/Spotify-API-Test.svg?style=flat-square&amp;label=Views&amp;labelColor=18181B&amp;color=0EA5E9&amp;logo=github" alt="Repository Views"/></a>
  <a href="https://github.com/power0matin/Spotify-API-Test/stargazers"><img src="https://img.shields.io/github/stars/power0matin/Spotify-API-Test?style=flat-square&amp;label=Stars&amp;labelColor=18181B&amp;color=F59E0B&amp;logo=github&amp;logoColor=white" alt="GitHub Stars"/></a>
  <a href="https://github.com/power0matin/Spotify-API-Test/forks"><img src="https://img.shields.io/github/forks/power0matin/Spotify-API-Test?style=flat-square&amp;label=Forks&amp;labelColor=18181B&amp;color=6366F1&amp;logo=github&amp;logoColor=white" alt="GitHub Forks"/></a>
  <a href="https://github.com/power0matin/Spotify-API-Test/issues"><img src="https://img.shields.io/github/issues/power0matin/Spotify-API-Test?style=flat-square&amp;label=Issues&amp;labelColor=18181B&amp;color=22C55E&amp;logo=github&amp;logoColor=white" alt="GitHub Issues"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/power0matin/Spotify-API-Test?style=flat-square&amp;label=License&amp;labelColor=18181B&amp;color=EF4444&amp;logo=github&amp;logoColor=white" alt="GitHub License"/></a>
</p>
<!-- repo-badges:end -->

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/github/repo-size/power0matin/Spotify-API-Test?style=flat&labelColor=333333&logoColor=E7E7E7&color=007BFF&label=Repo%20Size&logo=github"/>
  </a>
</p>

## 📝 Overview

`Spotify-API-Test` is a lightweight Python utility for testing **Spotify Web API authentication and connectivity** from a VPS, server, or hosting environment.

It uses Spotify's **Client Credentials flow** to request an access token from the Spotify OAuth endpoint and reports:

* HTTP status
* Request duration
* Token information (preview only)
* Authentication errors
* Detailed log output

The tool is useful for checking whether a server can successfully reach Spotify's authentication service and obtain an API token.

## ✨ Features

* ✅ Tests Spotify OAuth token endpoint accessibility.
* 🔐 Tests Spotify Client Credentials authentication.
* 📡 Measures request/response time.
* 🖥️ Provides a formatted terminal interface using `rich`.
* 🧾 Displays useful authentication and HTTP error information.
* 📝 Saves timestamped logs inside the `Log/` directory.
* 🔒 Only a short token preview is displayed/logged; the full access token is not exposed.
* 🧰 Lightweight and suitable for VPS diagnostics.
* 🧑‍💻 Designed and maintained by **power0matin**.

## 🛡️ Requirements

* 🐍 Python **3.7+**
* 📦 `requests`
* ✨ `rich` for the formatted terminal UI

`rich` is optional at runtime because the script falls back to plain terminal output when it is unavailable.

## 🔑 Spotify Credentials

The script requires a Spotify Developer application and uses the following environment variables:

```bash
SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET
```

You can create and manage Spotify applications from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

Set the credentials in your current shell before running the test:

```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

> ⚠️ Never commit your Spotify Client Secret to Git or place it directly inside the Python source code.

To verify that both variables are set:

```bash
test -n "$SPOTIFY_CLIENT_ID" && test -n "$SPOTIFY_CLIENT_SECRET" \
  && echo "Spotify credentials are configured." \
  || echo "Spotify credentials are missing."
```

## 📥 Installation

### Ubuntu / Debian

The recommended installation method is to use a Python virtual environment.

This avoids system-wide `pip` restrictions on modern Debian/Ubuntu systems and keeps the project dependencies isolated.

```bash
sudo apt update
sudo apt install -y git python3 python3-venv
```

Clone the repository:

```bash
git clone https://github.com/power0matin/Spotify-API-Test.git
cd Spotify-API-Test
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install requests rich
```

## ▶️ Run

First, configure your Spotify credentials:

```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

Then run the test:

```bash
python spotify_api_test.py
```

The script will:

1. Contact Spotify's OAuth token endpoint.
2. Authenticate using Client Credentials.
3. Measure the request duration.
4. Report the result in the terminal.
5. Save a detailed timestamped log in `Log/`.

Example:

```text
.venv/
spotify_api_test.py
Log/
└── spotify_api_test_2026-10-05_18-30-00.log
```

### Run Without Activating the Virtual Environment

Activation is optional. You can run the project directly through the virtual environment:

```bash
.venv/bin/python spotify_api_test.py
```

This is particularly convenient on VPS environments where you want a single command to execute the test.

## 🔄 Running Again Later

After the initial installation, you only need to enter the project directory, configure the credentials if they are not already exported, and run the script:

```bash
cd ~/Spotify-API-Test

export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"

.venv/bin/python spotify_api_test.py
```

## 📝 Logs

Every execution creates a timestamped log file in the `Log/` directory:

```text
Log/spotify_api_test_2026-10-05_18-30-00.log
```

The log contains information such as:

* Test start time
* Spotify token endpoint
* Authentication result
* HTTP status code
* Request duration
* Error details
* Token preview
* Token expiration information

## 🖥️ Example Output

### ✅ Successful Authentication

```text
Spotify API Connectivity Test

Status: ✅ Success
Token preview: BQC123456789...
Expires in: 3599 seconds
Request time: 0.214 seconds
Log file: Log/spotify_api_test_2026-10-05_18-30-00.log
```

### ❌ Authentication or Connectivity Error

```text
Spotify API Connectivity Test

Status: ❌ Failed
Error: Spotify token request failed with 401: ...
Log file: Log/spotify_api_test_2026-10-05_18-31-02.log
```

## 🧪 Troubleshooting

### `pip install` returns `externally-managed-environment`

This usually means you are trying to install packages into the system Python installation on a modern Debian/Ubuntu system.

Do not install the package globally. Create and use a virtual environment instead:

```bash
sudo apt install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests rich
```

### `python: command not found`

On many Ubuntu/Debian installations, the Python 3 executable is available as `python3` rather than `python`.

After creating the virtual environment, use:

```bash
python spotify_api_test.py
```

or without activation:

```bash
.venv/bin/python spotify_api_test.py
```

### `SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET is not configured`

Set both environment variables before running the script:

```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

### HTTP `401`

A `401` response generally indicates an authentication or credential problem.

Check that:

```bash
echo "$SPOTIFY_CLIENT_ID"
echo "$SPOTIFY_CLIENT_SECRET"
```

contain the expected values and that you copied the credentials correctly.

### HTTP `403`

A `403` means the request was rejected by Spotify. Do not automatically interpret every `403` as proof that the VPS IP is blocked.

Check the response/error details in the terminal output and the corresponding log file before diagnosing the cause.

### Connection or timeout errors

If the script cannot reach Spotify or the request times out, check:

```bash
curl -I https://accounts.spotify.com
```

You can also inspect DNS resolution:

```bash
getent hosts accounts.spotify.com
```

and test basic HTTPS connectivity:

```bash
curl -v https://accounts.spotify.com/api/token
```

## 📁 Project Structure

```text
Spotify-API-Test/
├── assets/
├── Log/
├── spotify_api_test.py
├── README.md
└── LICENSE
```

The `Log/` directory is created automatically when the script runs.

## 🤝 Contributing

Contributions, bug reports, issues, and feature requests are welcome.

To contribute:

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add new feature"
git push origin feature/your-feature
```

Then open a Pull Request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

**Matin Shahabadi (متین شاه‌آبادی / متین شاه آبادی)**

* Website: [matinshahabadi.ir](https://matinshahabadi.ir)
* Email: [me@matinshahabadi.ir](mailto:me@matinshahabadi.ir)
* GitHub: [power0matin](https://github.com/power0matin)
* LinkedIn: [matin-shahabadi](https://www.linkedin.com/in/matin-shahabadi)

<p align="center">
  © Created by <a href="https://github.com/power0matin">power0matin</a>
</p>
