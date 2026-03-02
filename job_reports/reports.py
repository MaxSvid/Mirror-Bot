import logging
from dataclasses import dataclass

import httpx
from bs4 import BeautifulSoup

DJINNI_URL = "https://djinni.co/jobs/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


@dataclass
class Job:
    title: str
    url: str


async def fetch_djinni_jobs(limit: int = 10) -> list[Job]:
    """Scrape latest job listings from Djinni."""
    async with httpx.AsyncClient(headers=HEADERS, timeout=15) as client:
        response = await client.get(DJINNI_URL)
        response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    job_links = soup.find_all("a", class_="job-item__title-link")[:limit]

    if not job_links:
        logging.warning("No job links found — Djinni HTML structure may have changed.")

    return [
        Job(title=a.get_text(strip=True), url="https://djinni.co" + a["href"])
        for a in job_links
    ]


def format_jobs_message(jobs: list[Job], source: str = "Djinni") -> str:
    if not jobs:
        return f"No jobs found on {source}."
    lines = [f"*Latest Jobs on {source}:*\n"]
    for i, job in enumerate(jobs, 1):
        lines.append(f"{i}. [{job.title}]({job.url})")
    return "\n".join(lines)
