import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    from app.main import main
    main()


if __name__ == "__main__":
    main()
