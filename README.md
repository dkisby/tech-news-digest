# 📰 Daily Tech News Digest to NotebookLM

This project automatically scrapes top tech news every morning and pushes it into a "Master" Google Doc, which I've connected to **NotebookLM** for instant AI summarization.



## 🚀 How it Works
1.  **Scrape:** A Python script (`main.py`) runs every morning via **GitHub Actions**. It pulls from RSS feeds like TLDR, Ars Technica, and The Verge.
2.  **Process:** The script formats the news into a clean text digest.
3.  **Push:** A second Python step in the workflow uses the **Google Docs API** to append this news to the very top of a specific Google Doc.
4.  **Analyze:** **NotebookLM** is synced to that Google Doc. I just hit "Refresh" in NotebookLM to get an AI briefing of the latest headlines.

## 🛠️ The Tech Stack
* **Python:** The engine (using `feedparser` and `google-api-python-client`).
* **GitHub Actions:** The scheduler (runs on a "cron" at 05:00 UTC).
* **Google OAuth2:** The security layer.
* **NotebookLM:** The "brain" that turns the raw text into a summary.

## 🔑 Setup & Secrets
To get this running, I had to:
* Enable **Google Drive** and **Google Docs** APIs in the Google Cloud Console.
* Generate OAuth credentials and use the **OAuth Playground**.
* Store the following in **GitHub Secrets**:
    * `DRIVE_REFRESH_TOKEN`
    * `MASTER_DOC_ID` (The ID found in the Google Doc URL).

## 💡 Why I Built This
* **Cut the Noise:** I wanted to stop visiting 10 different sites daily.
* **Persistence:** Instead of ephemeral emails, the news is saved in one long, searchable "Master Doc."
* **AI-Ready:** By feeding a single Google Doc into NotebookLM, I can ask questions like "What happened in AI regulation this week?" across months of data instantly.

---

### for Future Me:
If the upload ever fails with a `403`, the Google Refresh Token might have expired (though it shouldn't for personal apps in "Production" status) or the API might have been disabled in the Google Cloud Console. Re-run the OAuth Playground steps to fix.