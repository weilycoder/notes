import os
import sys
import argparse


def write_temp_settings(
    url: str,
    *,
    settings_file: str = "mkdocs.yml",
    temp_file: str = "mkdocs.temp.yml",
) -> None:
    with open(settings_file, "r", encoding="utf-8", newline="\n") as origin_settings:
        settings_content = origin_settings.read()
    settings_content = settings_content.replace("${SITE_URL}", url)
    with open(temp_file, "w", encoding="utf-8", newline="\n") as temp_settings:
        temp_settings.write(settings_content)


def main():
    parser = argparse.ArgumentParser(
        description="Build MkDocs site with a specific site URL.",
    )
    parser.add_argument(
        "command",
        metavar="COMMAND",
        type=str,
        help="The command to run.",
    )
    parser.add_argument(
        "url",
        metavar="URL",
        type=str,
        help="The site URL to use.",
    )

    args = parser.parse_args()
    write_temp_settings(args.url)
    os.system(f"mkdocs {args.command} -f mkdocs.temp.yml")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        if os.path.exists("mkdocs.temp.yml"):
            os.remove("mkdocs.temp.yml")
