from urllib.parse import parse_qs, urlparse


def extract_video_id(url: str) -> str:
    """Extract the YouTube video ID from common YouTube URL formats."""
    if not url:
        return ""

    parsed_url = urlparse(url)
    hostname = (parsed_url.hostname or "").lower()
    path_parts = [part for part in parsed_url.path.split("/") if part]

    if hostname == "youtu.be" and path_parts:
        return path_parts[0]

    if parsed_url.hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        if parsed_url.path == "/watch":
            params = parse_qs(parsed_url.query)
            if "v" in params:
                return params["v"][0]

        # Support links like /shorts/<id>, /embed/<id>, /live/<id>
        if len(path_parts) >= 2 and path_parts[0] in ("shorts", "embed", "live"):
            return path_parts[1]

    if "=" in url:
        return url.split("=")[1].split("&")[0]

    # If user pasted only the id, keep it unchanged.
    if len(url.strip()) == 11:
        return url.strip()

    return url
