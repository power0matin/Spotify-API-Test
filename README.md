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
    <img src="https://badges.strrl.dev/visits/power0matin/Spotify-API-Test?style=flat&labelColor=333333&logoColor=E7E7E7&label=Visits&logo=github" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/stars/power0matin/Spotify-API-Test?style=flat&labelColor=333333&logoColor=E7E7E7&color=EEAA00&label=Stars&logo=github"/>
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/repo-size/power0matin/Spotify-API-Test?style=flat&labelColor=333333&logoColor=E7E7E7&color=007BFF&label=Repo%20Size&logo=github"/>
  </a>
</p>


## 📝 Overview

`Spotify-API-Test` is a lightweight Python tool designed to **test Spotify API accessibility** from your VPS or hosting environment.
It sends a simple GET request to Spotify's OAuth token endpoint and logs response details such as **status code**, **headers**, and **response time** — perfect for debugging and connectivity verification.

📊 Use it to quickly check whether your VPS can reach Spotify without being blocked or rate-limited.


## ✨ Features

* ✅ Tests connection to Spotify OAuth token endpoint.
* 🧾 Logs status code, headers, and response time.
* 🕒 Saves logs in a timestamped file inside the `Log/` directory.
* 🧰 Minimal dependencies — just `requests`.
* 🧭 Helps diagnose VPS firewall or blocking issues.
* 🧑‍💻 Designed and maintained by **power0matin**.


## 🛡️ Requirements

* 🐍 **Python 3.7+**
* 📦 Python package: `requests`

  ```bash
  pip install requests
  ```


## 📥 Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/power0matin/Spotify-API-Test.git
   cd Spotify-API-Test
   ```

2. **Install dependencies**:

   ```bash
   pip install requests
   ```

3. **Run the test script**:

   ```bash
   python spotify_api_test.py
   ```

4. 📄 Check the console output and the generated log in the `Log/` directory.


## 🖥️ Example Output

```plaintext
[2025-08-11 08:03:27] ========================================
[2025-08-11 08:03:27] Designed by power0matin | GitHub: https://github.com/power0matin/Spotify-API-Test
[2025-08-11 08:03:27] Sending GET request to https://accounts.spotify.com/api/token
[2025-08-11 08:03:27] Status Code: 403
[2025-08-11 08:03:27] Response Time: 0.123 seconds
[2025-08-11 08:03:27] Response Headers:
[2025-08-11 08:03:27]   Content-Type: text/html; charset=UTF-8
[2025-08-11 08:03:27]   Referrer-Policy: no-referrer
[2025-08-11 08:03:27]   Content-Length: 304
[2025-08-11 08:03:27]   Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
[2025-08-11 08:03:27] ⛔ Forbidden: Spotify API access blocked on this VPS.

📝 Log has been saved to: Log/spotify_api_test_2025-08-11_08-03-27.log
```


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
To contribute:

1. Fork the repository.
2. Create your branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.


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
