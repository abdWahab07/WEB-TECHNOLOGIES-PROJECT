import shutil
import sys
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import Client

from bio.models import Bio

PUBLISH_DIR = Path(settings.BASE_DIR) / "netlify_publish"
STATIC_MAP = {
    "abdul-wahab": "index.html",
    "laiba-zainab": "laiba/index.html",
}


class Command(BaseCommand):
    help = "Export portfolio pages as static HTML for Netlify deployment."

    def handle(self, *args, **options):
        if not Bio.objects.exists():
            self.stderr.write(
                self.style.ERROR(
                    "No portfolio data found. Run migrations and add data first."
                )
            )
            sys.exit(1)

        if PUBLISH_DIR.exists():
            shutil.rmtree(PUBLISH_DIR)

        PUBLISH_DIR.mkdir(parents=True)
        client = Client(HTTP_HOST="127.0.0.1")
        exported = 0

        for slug, filename in STATIC_MAP.items():
            if not Bio.objects.filter(slug=slug).exists():
                continue

            if slug == "laiba-zainab":
                response = client.get("/laiba/", HTTP_HOST="127.0.0.1")
            else:
                response = client.get("/", HTTP_HOST="127.0.0.1")
            if response.status_code != 200:
                self.stderr.write(
                    self.style.ERROR(f"Failed to export {slug}: HTTP {response.status_code}")
                )
                continue

            html = response.content.decode("utf-8")
            output_path = PUBLISH_DIR / filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(html, encoding="utf-8")
            exported += 1
            self.stdout.write(f"Exported {slug} -> {output_path.relative_to(PUBLISH_DIR)}")

        if exported == 0:
            self.stderr.write(self.style.ERROR("No portfolio pages were exported."))
            sys.exit(1)

        self._copy_static_files()
        self._copy_media_files()
        self._write_redirects()
        self.stdout.write(self.style.SUCCESS(f"Static site ready in {PUBLISH_DIR}"))

    def _copy_static_files(self):
        static_src = Path(settings.BASE_DIR) / "static"
        static_dest = PUBLISH_DIR / "static"
        if static_src.exists():
            shutil.copytree(static_src, static_dest)

    def _copy_media_files(self):
        media_src = Path(settings.MEDIA_ROOT)
        media_dest = PUBLISH_DIR / "media"
        if media_src.exists():
            shutil.copytree(media_src, media_dest)

    def _write_redirects(self):
        redirects = [
            "/portfolio/abdul-wahab/  /  302",
            "/portfolio/laiba-zainab/  /laiba/  302",
            "/laiba  /laiba/  302",
        ]
        (PUBLISH_DIR / "_redirects").write_text("\n".join(redirects) + "\n", encoding="utf-8")
