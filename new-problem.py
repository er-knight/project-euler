import argparse
import pathlib

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    language_parser = parser.add_mutually_exclusive_group(required=True)
    language_parser.add_argument("--cpp", action="store_true")
    language_parser.add_argument("--py", action="store_true")
    
    language_extension = "cpp" if parser.parse_args().cpp else "py"

    PROBLEMS_DIR = pathlib.Path(__file__).parent / "problems"
    TOTAL_PROBLEMS_FILES = len(tuple(PROBLEMS_DIR.iterdir()))
    PROBLEMS_FILE_MODE   = int(oct(tuple(PROBLEMS_DIR.iterdir())[0].stat().st_mode)[-3:], base=8)
    
    (PROBLEMS_DIR / f"problem-{TOTAL_PROBLEMS_FILES + 1}.md").touch(mode=PROBLEMS_FILE_MODE, exist_ok=True)

    SOLUTIONS_DIR = pathlib.Path(__file__).parent / "solutions"
    SOLUTIONS_FILE_MODE = int(oct(tuple(SOLUTIONS_DIR.iterdir())[0].stat().st_mode)[-3:], base=8)
    
    (SOLUTIONS_DIR / f"problem-{TOTAL_PROBLEMS_FILES + 1}.{language_extension}").touch(mode=PROBLEMS_FILE_MODE, exist_ok=True)