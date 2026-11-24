import os

LINE = "★★★★☆ Four stars. He gives orders one word at a time, usually at 3 a.m. — 'Gas.' On that single syllable I have minted a hundred NFTs and entered fifty contests. Would be five stars if he ever slept."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
